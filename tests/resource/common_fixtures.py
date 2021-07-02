import base64
import copy
from dataclasses import dataclass

import allure
import pytest

from tests import CommonTests

ROUTE_FILE = 'tests/exchangeRoutes/test_files/test_voyage_plan.xml'

STATUS_WO_INACTIVE_LIST = [1, 2, 3, 7]
STATUS_WO_INACTIVE_IDS = [f'Status - {s}' for s in STATUS_WO_INACTIVE_LIST]

common_tests = CommonTests()


@pytest.fixture(params=STATUS_WO_INACTIVE_LIST, ids=STATUS_WO_INACTIVE_IDS)
def res_test_data_route(request, connection_route_1):
    """Подготовка тестовых данных Маршрутов для сервиса обмена маршрутов"""
    @dataclass
    class DataItems:
        identities_list: any
        uvid: any
        route_tree: any
        route_str: any
        route_inactive_str: any
        route_next_status_str: any
        routes_base64_list: any
        routes_inactive_base64_list: any
        routes_next_status_base64_list: any

    with allure.step('Setup Step 1. Подготовка переменных'):
        # TODO: Переделать авторизацию сущностей через получение ID из хедеров
        identities_list = [
            {'identityId': 'urn:mrn:mcp:service:instance:knsb:test-service-test1', 'identityName': 'test11'}]
        uvid = common_tests.RES_DATA_ROUTES.generate_uvid()
        route_tree = common_tests.RES_DATA_ROUTES.get_route_from_file(path_route=ROUTE_FILE)
        route_tree = common_tests.RES_DATA_ROUTES.change_uvid_in_route(tree_route=route_tree,
                                                                       uvid=uvid)
        route_tree = common_tests.RES_DATA_ROUTES.change_status_in_route(tree_route=route_tree,
                                                                         status=request.param)
        route_inactive_tree = common_tests.RES_DATA_ROUTES.change_status_in_route(tree_route=route_tree,
                                                                                  status=8)
        route_next_status_tree = common_tests.RES_DATA_ROUTES.change_status_in_route(tree_route=route_tree,
                                                                                     status=request.param + 1)
        route_str = common_tests.RES_DATA_ROUTES.convert_route_to_str(route_tree)
        route_inactive_str = common_tests.RES_DATA_ROUTES.convert_route_to_str(route_inactive_tree)
        route_next_status_str = common_tests.RES_DATA_ROUTES.convert_route_to_str(route_next_status_tree)

    with allure.step('Setup Step 2. Добавить маршрут.'):
        common_tests.RES_PRIVATE_ROUTES.published_routes(
            session=connection_route_1,
            routes=route_str)

    with allure.step('Setup Step 3. Авторизовать субъект на маршрут'):
        common_tests.RES_PRIVATE_AUTHORIZE.add_authorized_identities_from_route_by_uvid(
            session=connection_route_1,
            uvid=uvid,
            authorized_identities=identities_list)

    return DataItems(identities_list=identities_list,
                     uvid=uvid,
                     route_tree=route_tree,
                     route_str=route_str,
                     route_inactive_str=route_inactive_str,
                     route_next_status_str=route_next_status_str,
                     routes_base64_list=[{'route': base64.standard_b64encode(route_str).decode("utf-8")}],
                     routes_inactive_base64_list=[
                         {'route': base64.standard_b64encode(route_inactive_str).decode("utf-8")}],
                     routes_next_status_base64_list=[
                         {'route': base64.standard_b64encode(route_next_status_str).decode("utf-8")}])


@pytest.fixture(scope='session', params=[1, 2, 10])
def res_test_data_subscription(request):
    """Подготовка тестовых данных Подписчиков для сервиса обмена маршрутов"""

    @dataclass
    class TestData:
        subscriptions_list: any
        subscriptions_list_other: any
        subscriptions_list_other_url: any
        subscriptions_list_other_name: any

    subscriptions_list = common_tests.RES_DATA_SUBSCRIPTIONS.get_random_subscriptions_list(count=request.param)

    second_subscriptions_list = common_tests.RES_DATA_SUBSCRIPTIONS.get_random_subscriptions_list(count=request.param)
    subscriptions_list_other_url = copy.deepcopy(subscriptions_list)
    subscriptions_list_other_name = copy.deepcopy(subscriptions_list)
    for i in range(len(subscriptions_list)):
        subscriptions_list_other_url[i]['endpointURL'] = second_subscriptions_list[i]['endpointURL']
        subscriptions_list_other_name[i]['identityName'] = second_subscriptions_list[i]['identityName']

    return TestData(subscriptions_list=subscriptions_list,
                    subscriptions_list_other=common_tests.RES_DATA_SUBSCRIPTIONS.get_random_subscriptions_list(count=request.param),
                    subscriptions_list_other_url=subscriptions_list_other_url,
                    subscriptions_list_other_name=subscriptions_list_other_name)


@pytest.fixture(scope='session', params=[1, 2, 10])
def res_test_data_identities(request):
    """Подготовка тестовых данных Списка авторизации"""
    @dataclass
    class TestData:
        idents_list: any
        idents_list_other_name: any

    idents_list = common_tests.RES_DATA_AUTHORIZE.get_random_identities_list(count=request.param)
    second_idents_list = common_tests.RES_DATA_AUTHORIZE.get_random_identities_list(count=request.param)

    idents_list_other_name = copy.deepcopy(idents_list)
    for i in range(len(idents_list_other_name)):
        idents_list_other_name[i]['identityName'] = second_idents_list[i]['identityName']

    return TestData(idents_list=idents_list,
                    idents_list_other_name=idents_list_other_name)
