import allure

from tests import CommonTests


@allure.feature("Routes - Private API")
@allure.story("Публикация нового маршрута")
class TestPublishedRoute(CommonTests):

    ROUTE_FILE = "tests/exchangeRoutes/test_files/test_voyage_plan.xml"

    def test_published_new_routes(self, connection_route_1):
        with allure.step("Step 1. Добавление маршрутa."):
            tree_route = self.RES_DATA_ROUTES.get_route_from_file(path_route=self.ROUTE_FILE)

            tree_route = self.RES_DATA_ROUTES.change_uvid_in_route(tree_route=tree_route,
                                                                   uvid=self.RES_DATA_ROUTES.generate_uvid())
            self.RES_PRIVATE_ROUTES.published_routes(session=connection_route_1,
                                                     routes=self.RES_DATA_ROUTES.convert_route_to_str(tree_route))
