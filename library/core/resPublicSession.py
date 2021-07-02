import functools
import logging
import requests

from http import HTTPStatus


def reauthorize_on_401(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        response = method(self, *args, **kwargs)
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            logging.info(f"UNAUTHORIZED")
            response = method(self, *args, **kwargs)
        return response
    return wrapper


class ResPublicSession(requests.Session):

    def __init__(self, host):
        super().__init__(host)
        self.add_cert()

    def add_cert(self):
        cert = ""
        self.headers.update({"X-Client-Certificate": cert})

    @reauthorize_on_401
    def do_get(self, **kwargs):
        return super().do_get(**kwargs)
