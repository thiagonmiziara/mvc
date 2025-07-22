from unittest import mock
import pytest
from sqlalchemy.orm.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                        PetsTable(name="Buddy", type="Dog"),
                        PetsTable(name="Mittens", type="Cat"),
                    ],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass


class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass


def test_list_pets():
    mock_connection = MockConnection()
    repository = PetsRepository(mock_connection)
    response = repository.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert len(response) == 2
    assert response[0].name == "Buddy"
    assert response[1].type == "Cat"


def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    repository = PetsRepository(mock_connection)
    response = repository.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert len(response) == 0
    assert response == []


def test_delete_pets():
    mock_connection = MockConnection()
    repository = PetsRepository(mock_connection)

    repository.delete_pets("Buddy")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "Buddy")
    mock_connection.session.delete.assert_called_once()


def test_delete_pets_error():
    mock_connection = MockConnectionNoResult()
    repository = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repository.delete_pets("Buddy")

    mock_connection.session.rollback.assert_called_once()
