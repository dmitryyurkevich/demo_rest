import logging
import requests
import socket
from requests import HTTPError, RequestException, Timeout, ConnectionError

from validators import url as url_validator

HTTP_METHOD_NAMES = ("get", "post", "put", "patch", "delete",)
REQUEST_EXCEPTIONS_AND_ERRORS = (HTTPError, ConnectionError, RequestException, Timeout)


def do_request(method, url, **kwargs):
    if not url_validator(url):
        raise RuntimeError(f"invalid url: {url}")

    if not callable(method):
        method = method.lower()
        if method not in HTTP_METHOD_NAMES:
            raise RuntimeError(f"No such http request method: {method}")

        method = getattr(requests, method)

    logging.info(f"{method.__name__}: {socket.gethostname()} >>> {url}")
    logging.info(f"headers: {kwargs.get('headers', None)}")
    logging.info(f"params: {kwargs.get('params', None)}")
    logging.info(f"body: {kwargs.get('data', None)}")

    try:
        response = method(url=url, **kwargs)

        logging.info(f"status: {response.status_code}")
        logging.info(f"response: {response.text}")
        return response

    except REQUEST_EXCEPTIONS_AND_ERRORS as e:
        logging.info(f"can not perform {method.__name__} request to {url}\n{e}")


def get_payload(**kwargs):
    if kwargs:
        return kwargs
