
# NOTE: not fit for public distribution until we have a public auth client
from authclient import Client as AuthClient
from authclient.config import Config as AuthConfig

from .config import Config
from .rest import Rest


class AuthRequester(object):
    """ Wraps the RealMassive AuthClient with HTTP request methods.
    """
    def __init__(self, user=None, password=None, config=None):
        self.client = AuthClient(user, password, config=config)

    def _request(self, method, **kwargs):
        url = kwargs.pop("url")
        request = dict(method=method, url=url, **kwargs)
        return self.client.request(request)

    def delete(self, **kwargs):
        return self._request("DELETE", **kwargs)

    def get(self, **kwargs):
        return self._request("GET", **kwargs)

    def head(self, **kwargs):
        return self._request("HEAD", **kwargs)

    def options(self, **kwargs):
        return self._request("OPTIONS", **kwargs)

    def patch(self, **kwargs):
        return self._request("PATCH", **kwargs)

    def post(self, **kwargs):
        return self._request("POST", **kwargs)

    def put(self, **kwargs):
        return self._request("PUT", **kwargs)


class RealMassive(Rest):
    """ The RealMassive Python SDK makes authenticated requests!

        1) Pass in the RealMassive API base endpoint as `domain`
        2) Pass in a HTTP request client as `requester`
        3) Make requests!
    """

    def __init__(self, domain=Config.ENDPOINT, requester=None):
        if not requester:
            AuthConfig.ENDPOINT = Config.AUTH_ENDPOINT
            requester = AuthRequester(
                user=Config.USER,
                password=Config.PASSWORD,
                config=AuthConfig
            )

        super(RealMassive, self).__init__(path=domain, requester=requester)
