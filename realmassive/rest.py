
from functools import partial
import unittest


class Rest(object):

    def __init__(self, path='', requester=None):
        self._path = [path]
        self._requester = requester

    @staticmethod
    def _is_http_method(name):
        return name in {'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS'}

    def _new(self):
        return Rest(path=str(self), requester=self._requester)

    def __str__(self):
        return '/'.join(self._path)

    def __repr__(self):
        return str(self)

    def __call__(self, *args):
        path = map(str, args)
        new = self._new()
        new._path.extend(path)
        return new

    def __getattr__(self, name):
        if name.startswith('__'):
            return self.__getattribute__(name)
        if self._is_http_method(name):
            method = getattr(self._requester, name.lower())
            return partial(method, url=str(self))
        else:
            new = self._new()
            new._path.append(name)
            return new

