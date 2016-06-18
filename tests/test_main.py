
import mock
from unittest import TestCase

from realmassive_sdk import AuthRequester, RealMassive


KWARGS = {
    "url": "https://www.example.com",
    "params": {
        "bacon": "cheese"
    },
    "lol": "test"
}


class TestAuthRequester(TestCase):

    @mock.patch("realmassive_sdk.AuthClient")
    def setUp(self, authclient_mock):
        self.requester = AuthRequester(
            user="test@example.com",
            password="foobar",
            config=mock.MagicMock(),
        )

    def test__request(self):
        method = "GET"
        self.requester._request(
            method,
            **KWARGS
        )
        self.requester.client.request.assert_called_with(
            dict(method="GET", **KWARGS)
        )

    def test_delete(self):
        self.requester.delete(**KWARGS)
        self.requester.client.request.assert_called_with(
            dict(method="DELETE", **KWARGS)
        )

    def test_get(self):
        self.requester.get(**KWARGS)
        self.requester.client.request.assert_called_with(
            dict(method="GET", **KWARGS)
        )

    def test_head(self):
        self.requester.head(**KWARGS)
        self.requester.client.request.assert_called_with(
            dict(method="HEAD", **KWARGS)
        )

    def test_options(self):
        self.requester.options(**KWARGS)
        self.requester.client.request.assert_called_with(
            dict(method="OPTIONS", **KWARGS)
        )

    def test_patch(self):
        self.requester.patch(**KWARGS)
        self.requester.client.request.assert_called_with(
            dict(method="PATCH", **KWARGS)
        )

    def test_post(self):
        self.requester.post(**KWARGS)
        self.requester.client.request.assert_called_with(
            dict(method="POST", **KWARGS)
        )

    def test_put(self):
        self.requester.put(**KWARGS)
        self.requester.client.request.assert_called_with(
            dict(method="PUT", **KWARGS)
        )
