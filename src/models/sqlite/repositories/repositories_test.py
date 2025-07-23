import pytest
from src.models.sqlite.settings.conection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

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

    repository.delete_pets(name)


@pytest.mark.skip(reason="interactive database test")
def test_insert_person():
    first_name = "John"
    last_name = "Doe"
    age = 30
    pet_id = 1
    repository = PeopleRepository(db_connection_handler)
    repository.insert_person(first_name, last_name, age, pet_id)


@pytest.mark.skip(reason="interactive database test")
def test_get_person():
    person_id = 1

    repository = PeopleRepository(db_connection_handler)
    response = repository.get_person(person_id)
    print()
    print(response)
