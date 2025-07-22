import pytest
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.conection import db_connection_handler

# db_connection_handler.conect_to_db()


@pytest.mark.skip(reason="interactive database test")
def test_list_pets():
    repository = PetsRepository(db_connection_handler)
    pets = repository.list_pets()
    assert isinstance(pets, list)


@pytest.mark.skip(reason="interactive database test")
def test_delete_pet():
    name = "belinha"
    repository = PetsRepository(db_connection_handler)
    # Assuming there is a pet named 'Fido' in the database
    repository.delete_pets(name)
