
# NOTE: not fit for public distribution until we have a public auth client
from authclient import Client
from authclient.config import Config as AuthConfig
from hammock import Hammock

from .config import Config


class RealMassive(Hammock):
    """ Custom Hammock instance that uses our auth client.
    """
    def __init__(self, parent=None, append_slash=False, config=Config):
        """ Overriding Hammocks __init__ to use the RealMassive auth client
            instead of a requests.session.

            Arguments:
                name -- name of node
                parent -- parent node for chaining
                append_slash -- flag if you want a trailing slash in urls

            Optional arguments:
                session -- an initialized RM auth client. If not provided,
                    will attempt to use credentials stored as environment
                    variables: REALMASSIVE_USER and REALMASSIVE_PASSWORD
        """
        # Setup Hammock
        self._name = config.ENDPOINT
        self._parent = parent
        self._append_slash = append_slash

        # Setup Auth
        AuthConfig.ENDPOINT = config.AUTH_ENDPOINT
        self._session = Client(
            config.USER,
            config.PASSWORD,
            config=AuthConfig
        )

    def _request(self, method, *args, **kwargs):
        """ Make HTTP request using RM auth client.
        """
        request = dict(method=method.upper(), url=self._url(*args), **kwargs)
        return self._session.request(request)

    def _close_session(self):
        """ Log out.
        """
        self._session.logout()

    def logout(self):
        """ Log out.
        """
        self._close_session()
