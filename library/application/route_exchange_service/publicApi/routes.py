from library.application.route_exchange_service.common import Common


class PublicRoutes(Common):
    """Класс для работы с публичным API маршрутов"""

    def __init__(self):
        self.uri = f'{Common.public_api_uri}/published-routes'

    def get_routes(self, session, uvid=None, route_status=None, expected_status=Common.HTTPStatus.OK):
        """Запрос маршрута
        :param session: Сессия сервиса
        :param uvid: Идентификатор маршрута
        :param route_status: Статус маршрута
        :param expected_status: Ожидаемый статус ответа
        """
        params = {}
        if route_status:
            params.update({'routeStatus': route_status})
        if uvid:
            params.update({'uvid': uvid})
        response = session.do_get(path=self.uri, params=params, expected_status=expected_status)
        return response.json()

    def upload_routes(self, session, route, delivery_ack_endpoint=None, callback_endpoint=None,
                      expected_status=Common.HTTPStatus.NO_CONTENT):
        """Принятие и ретрансляция маршрута
        :param session: Сессия сервиса
        :param route: План в RTZ формате
        :param delivery_ack_endpoint: URL-адрес подтверждения доставки
        :param callback_endpoint: URL-адрес ответной пересылки маршрута
        :param expected_status: Ожидаемый статус ответа
        :return:
        """
        params = {}
        data = {
            'voyagePlan': route
        }
        if delivery_ack_endpoint:
            params.update({'deliveryAckEndPoint': delivery_ack_endpoint})
        if callback_endpoint:
            params.update({'callbackEndpoint': callback_endpoint})
        response = session.do_post(path=self.uri, params=params, data=data,
                                   expected_status=expected_status)
        return response.json()
