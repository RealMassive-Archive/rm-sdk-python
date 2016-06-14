
# NOTE: not fit for public distribution until we have a public auth client
from authclient import Client
from authclient.config import Config as AuthConfig

from .config import Config
from .rest import Rest


class Requester(object):
    """ Make requests through a given client.
    """

    def __init__(self, client):
        self.client = client

    def _request(self, method, *args, **kwargs):
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

        1) Set your config environment variables or object
        2) Initialize this class
        3) Make requests!
    """
    def __init__(self, domain=None, config=Config):
        if not domain:
            domain = config.ENDPOINT

        # Setup Auth
        AuthConfig.ENDPOINT = config.AUTH_ENDPOINT
        auth_client = Client(
            config.USER,
            config.PASSWORD,
            config=AuthConfig
        )
        requester = Requester(auth_client)
        super(RealMassive, self).__init__(path=domain, requester=requester)
