import unittest
from unittest.mock import Mock
from src.views.person_finder_view import PersonFinderView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.person_finder_controller import (
    PersonFinderControllerInterface,
)


class TestPersonFinderView(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_controller = Mock(spec=PersonFinderControllerInterface)
        self.person_finder_view = PersonFinderView(self.mock_controller)

    def test_handle(self) -> None:
        mock_request_param = {"person_id": "123"}
        mock_http_request = HttpRequest(param=mock_request_param)

        mock_controller_response = {
            "success": True,
            "data": {"id": 123, "name": "Jane Doe"},
        }
        self.mock_controller.find.return_value = mock_controller_response

        response = self.person_finder_view.handle(mock_http_request)

        self.mock_controller.find.assert_called_once_with(
            mock_request_param["person_id"]
        )
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.body, mock_controller_response)
