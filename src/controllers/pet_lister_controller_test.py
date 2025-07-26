from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController


class MockPetsRepository:
    def list_pets(self) -> list[PetsTable]:
        return [
            PetsTable(id=1, name="Buddy", type="Dog"),
            PetsTable(id=2, name="Mittens", type="Cat"),
        ]


def test_list_pets():
    controller = PetListerController(MockPetsRepository())

    response = controller.list()

    assert response == {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"id": 1, "name": "Buddy", "type": "Dog"},
                {"id": 2, "name": "Mittens", "type": "Cat"},
            ],
        }
    }
