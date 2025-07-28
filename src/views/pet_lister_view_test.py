import unittest
from unittest.mock import Mock
from src.views.pet_lister_view import PetListerView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pet_lister_controller import (
    PetListerControllerInterface,
)


class TestPetListerView(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_controller = Mock(spec=PetListerControllerInterface)
        self.pet_lister_view = PetListerView(self.mock_controller)

    def test_handle(self) -> None:
        mock_http_request = HttpRequest()

        mock_controller_response = {
            "success": True,
            "data": [{"id": 1, "name": "Dog"}, {"id": 2, "name": "Cat"}],
        }
        self.mock_controller.list.return_value = mock_controller_response

        response = self.pet_lister_view.handle(mock_http_request)

        self.mock_controller.list.assert_called_once()
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.body, mock_controller_response)
