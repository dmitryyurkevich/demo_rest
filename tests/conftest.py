from dataclasses import dataclass

import allure
import logging
import pytest

from library import application, asserts, data, core

HOST_ROUTE_SERVICE_1 = "http://localhost:8080"
HOST_ROUTE_SERVICE_2 = "http://localhost:8081"
ROUTE_FILE_DEFAULT = "tests/exchangeRoutes/test_files/test_voyage_plan.xml"

pytest_plugins = ["tests.resource.common_fixtures", ]


@pytest.fixture(scope="session")
def connection_route_1():
    with core.Session(host=HOST_ROUTE_SERVICE_1) as session:
        yield session


@pytest.fixture(scope="session")
def connection_route_1_public():
    with core.ResPublicSession(host=HOST_ROUTE_SERVICE_1) as session:
        yield session


@pytest.fixture()
def unique_uvid():
    return data.route_exchange_service.DataRoutes().generate_uvid()


# Обертка для логгирования через алюр
class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step(f"Log {message}"):
            pass

    def emit(self, record):
        self.log(f"({record.levelname}) {record.getMessage()}")


class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()

    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)

    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    with AllureCatchLogs():
        yield
