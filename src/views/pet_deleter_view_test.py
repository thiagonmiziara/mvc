import unittest
from unittest.mock import Mock
from src.views.pet_deleter_view import PetDeleterView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pet_deleter_controller import (
    PetDeleterControllerInterface,
)


class TestPetDeleterView(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_controller = Mock(spec=PetDeleterControllerInterface)
        self.pet_deleter_view = PetDeleterView(self.mock_controller)

    def test_handle(self) -> None:
        mock_request_param = {"name": "Fido"}
        mock_http_request = HttpRequest(param=mock_request_param)

        response = self.pet_deleter_view.handle(mock_http_request)

        self.mock_controller.delete.assert_called_once_with(mock_request_param["name"])
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(response.body)
