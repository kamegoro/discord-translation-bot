import unittest
from unittest import mock

from api.api_request import make_api_request


class MakeApiRequestTest(unittest.TestCase):
    @mock.patch("api.api_request.requests.get")
    def test_returns_json_on_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"ok": True}

        self.assertEqual(make_api_request("https://example.com"), {"ok": True})
        mock_get.assert_called_once_with("https://example.com")

    @mock.patch("api.api_request.requests.get")
    def test_returns_none_on_error_status(self, mock_get):
        mock_get.return_value.status_code = 500

        self.assertIsNone(make_api_request("https://example.com"))


if __name__ == "__main__":
    unittest.main()
