from typing import Dict
import re
from src.controllers.interfaces.person_creator_controller import (
    PersonCreatorControllerInterface,
)
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, person_info: Dict) -> Dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validade_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        formated_response = self.__format_resoponse(person_info)
        return formated_response

    def __validade_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expression to match non-alphabetic characters
        non_valid_caracteres = re.compile(r"[^a-zA-Z]")

        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(
            last_name
        ):
            raise Exception("Nome da pessoa inválido. Deve conter apenas letras.")

    def __insert_person_in_db(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_resoponse(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info,
            }
        }
