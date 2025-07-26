from typing import Dict, List
from src.controllers.interfaces.pet_lister_controller import (
    PetListerControllerInterface,
)
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable


class PetListerController(PetListerControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface):
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append(
                {
                    "id": pet.id,
                    "name": pet.name,
                    "type": pet.type,
                }
            )

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets,
            }
        }
