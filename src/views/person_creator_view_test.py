import unittest
from unittest.mock import Mock
from src.views.person_creator_view import PersonCreatorView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.person_creator_controller import (
    PersonCreatorControllerInterface,
)


class TestPersonCreatorView(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_controller = Mock(spec=PersonCreatorControllerInterface)
        self.person_creator_view = PersonCreatorView(self.mock_controller)

    def test_handle(self) -> None:
        mock_request_body = {"name": "John Doe", "age": 30, "pet_id": 123}
        mock_http_request = HttpRequest(body=mock_request_body)

        mock_controller_response = {
            "success": True,
            "data": {"id": 1, "name": "John Doe"},
        }
        self.mock_controller.create.return_value = mock_controller_response

        response = self.person_creator_view.handle(mock_http_request)

        self.mock_controller.create.assert_called_once_with(mock_request_body)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.body, mock_controller_response)
