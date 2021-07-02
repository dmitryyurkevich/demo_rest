import allure

from tests import CommonTests


@allure.feature("Routes - Public API")
class TestPublicPublishedRoute(CommonTests):
    @allure.story("Получение опубликованного маршрута, есть права на маршрут")
    def test_get_all_authorized_route(self, connection_route_1_public, res_test_data_route):
        with allure.step("Step 1. Получить маршрут"):
            routes_info = self.RES_PUBLIC_ROUTES.get_routes(session=connection_route_1_public)

        with allure.step("Step 2. Проверить полученый маршрут"):
            routes_list = routes_info.get("voyagePlans", [])
            assert len(routes_list) > 0, "Количество полученных маршрутов равно 0"
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=routes_list,
                expected_list=res_test_data_route.routes_base64_list), \
                "Искомый маршрут не найден."

    @allure.story("Прекращение получение маршрута после публикации в статусе INACTIVE, есть права на маршрут")
    def test_try_get_inactive_authorized_route(self, connection_route_1, connection_route_1_public, res_test_data_route):
        """MCP-1063"""
        with allure.step("Step 1. Получить маршруты."):
            routes_info = self.RES_PUBLIC_ROUTES.get_routes(session=connection_route_1_public)

        with allure.step("Step 2. Проверить полученые маршруты"):
            routes_list = routes_info.get("voyagePlans", [])
            assert len(routes_list) > 0, "Количество полученных маршрутов равно 0"
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=routes_list,
                expected_list=res_test_data_route.routes_base64_list), \
                "Искомый маршрут не найден."

        with allure.step("Step 3. Добавить маршрут в статусе INACTIVE."):
            self.RES_PRIVATE_ROUTES.published_routes(
                session=connection_route_1,
                routes=res_test_data_route.route_inactive_str)

        with allure.step("Step 4. Получить маршруты."):
            routes_info = self.RES_PUBLIC_ROUTES.get_routes(session=connection_route_1_public)

        with allure.step("Step 2. Проверить полученые маршруты"):
            routes_list = routes_info.get("voyagePlans", [])
            assert not self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=routes_list,
                expected_list=res_test_data_route.routes_inactive_base64_list), \
                "Маршрут не пропал из списка получаемых."

    @allure.story("Получение последнего опубликованного маршрута (включая неактивный), есть права на маршрут")
    def test_get_last_authorized_route(self, connection_route_1, connection_route_1_public, res_test_data_route):
        """MCP-1063"""
        with allure.step("Step 1. Получить маршруты."):
            routes_info = self.RES_PUBLIC_ROUTES.get_routes(
                session=connection_route_1_public,
                uvid=res_test_data_route.uvid)

        with allure.step("Step 2. Проверить полученые маршруты"):
            routes_list = routes_info.get("voyagePlans", [])
            assert len(routes_list) == 1, "Количество полученных маршрутов не равно 1"
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=routes_list,
                expected_list=res_test_data_route.routes_base64_list), \
                "Искомый маршрут не найден."

        with allure.step("Step 3. Добавить маршрут в следующем по порядку статусе."):
            self.RES_PRIVATE_ROUTES.published_routes(
                session=connection_route_1,
                routes=res_test_data_route.route_next_status_str)

        with allure.step("Step 4. Получить маршруты."):
            routes_info = self.RES_PUBLIC_ROUTES.get_routes(
                session=connection_route_1_public,
                uvid=res_test_data_route.uvid)

        with allure.step("Step 2. Проверить полученые маршруты"):
            routes_list = routes_info.get("voyagePlans", [])
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=routes_list,
                expected_list=res_test_data_route.routes_next_status_base64_list), \
                "Искомый маршрут не найден."
