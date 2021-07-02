from library.application.route_exchange_service.common import Common


class PrivateRoutes(Common):
    """Класс для работы с приватным API маршрутов"""

    def __init__(self):
        self.path = f"{Common.res_private_api_uri}/published-routes"

    def published_routes(self, session, routes):
        """Публикация маршрута
        :param session: Сессия сервиса
        :param routes: Маршрут в формате RTZ
        """
        return session.do_post(path=self.path, data=routes, headers=Common.headers_xml,
                               expected_status=Common.HTTPStatus.NO_CONTENT)
