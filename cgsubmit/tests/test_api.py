import unittest
from cgsubmit.api import Api
from unittest.mock import MagicMock
import mock


class TestApi(unittest.TestCase):
    @mock.patch("cgsubmit.api.api.requests")
    def test_get_all_battles(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = "mocked result"
        mock_requests.post.return_value = mock_response
        api = Api("test-session-handle")
        self.assertEqual(api.test_session_handle, "test-session-handle")
        self.assertEqual(api.get_all_battles(), "mocked result")

        mock_response.status_code = 500
        try:
            api.get_all_battles()
        except Exception as exception:
            self.assertTrue(
                str(exception).startswith("Unable to retrieve last battles: ")
            )
            pass
        else:
            self.fail("Exception not raised")

    @mock.patch("cgsubmit.api.api.requests")
    def test_get_lost_games(self, mock_requests):
        mock_response = MagicMock()
        mock_response.json.return_value = "mocked result"
        mock_requests.post.return_value = mock_response
        api = Api("")
        self.assertEqual(
            api.get_lost_games([1, 2, 3]),
            ["mocked result", "mocked result", "mocked result"],
        )
