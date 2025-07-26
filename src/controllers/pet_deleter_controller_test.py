from .pet_deleter_controller import PetDeleterController


def test_delete_pet(mocker):
    mock_reopository = mocker.Mock()
    controller = PetDeleterController(mock_reopository)
    controller.delete("Buddy")

    mock_reopository.delete_pets.assert_called_once_with("Buddy")
