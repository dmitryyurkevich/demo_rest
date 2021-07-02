from library.application.route_exchange_service.common import Common


class PrivateRemoteService(Common):
    """Класс для работы с приватным API запросов к удаленым сервисам"""

    def __init__(self):
        self.base_path = f"{Common.res_private_api_uri}/remote-services"

    def post_acknowledgements(self, session, delivery_ack_endpoint, delivery_ack,
                              expected_status=Common.HTTPStatus.NO_CONTENT):
        """Посылает подтверждение, что маршрут принят.
        :param session: Сессия сервиса
        :param delivery_ack_endpoint: URL-адрес подтверждения доставки
        :param delivery_ack: Подтверждение принятия маршрута
        :param expected_status: Ожидаемый статус ответа
        :return:
        """
        params = {"deliveryAckEndPoint ": delivery_ack_endpoint}

        session.do_post(path=f"{self.base_path}/acknowledgements", params=params, data=delivery_ack,
                        expected_status=expected_status)

    def post_subscriptions(self, session, publisher_endpoint, uvid=None, expected_status=Common.HTTPStatus.NO_CONTENT):
        """Подписывается на получение маршрутов, публикуемых сторонним сервисом.
        :param session: Сессия сервиса
        :param publisher_endpoint: URL-адрес сервиса, публикующего маршруты
        :param uvid: Идентификатор маршрута
        :param expected_status: Ожидаемый статус ответа
        :return:
        """
        params = {"uvid ": uvid} if uvid else {}
        params.update({"publisherEndpoint": publisher_endpoint})
        session.do_post(path=f"{self.base_path}/subscriptions", params=params, expected_status=expected_status)

    def del_subscriptions(self, session, publisher_endpoint, uvid=None, expected_status=Common.HTTPStatus.NO_CONTENT):
        """Аннулирует созданную ранее свою подписку на получение маршрутов, публикуемых сторонним сервисом.
        :param session: Сессия сервиса
        :param publisher_endpoint: URL-адрес сервиса, публикующего маршруты
        :param uvid: Идентификатор маршрута
        :param expected_status: Ожидаемый статус ответа
        :return:
        """
        params = {"uvid ": uvid} if uvid else {}
        params.update({"publisherEndpoint": publisher_endpoint})
        session.do_delete(path=f"{self.base_path}/subscriptions", params=params, expected_status=expected_status)

    def get_published_routes(self, session, publisher_endpoint, uvid=None, route_status=None,
                             expected_status=Common.HTTPStatus.OK):
        """Возвращает список маршрутов, опубликованных удаленным сервисом к которым запрашивающая сторона имеет право
        доступа.
        :param session: Сессия сервиса
        :param publisher_endpoint: URL-адрес сервиса, публикующего маршруты
        :param uvid: Идентификатор маршрута
        :param route_status: Статус маршрута
        :param expected_status: Ожидаемый статус ответа
        :return:
        """
        params = {"publisherEndpoint": publisher_endpoint}
        params.update({"uvid": uvid} if uvid else {})
        params.update({"routeStatus": route_status} if route_status else {})
        return session.do_get(path=f"{self.base_path}/published-routes", params=params,
                              expected_status=expected_status).json()

    def post_uploaded_routes(self, session, route, target_endpoint, delivery_ack_required, callback_required=None,
                             expected_status=Common.HTTPStatus.NO_CONTENT):
        """Посылает маршрут конкретному клиенту-получателю.
        :param session: Сессия сервиса
        :param route: План в RTZ формате
        :param target_endpoint: URL-адрес получателя маршрута
        :param delivery_ack_required: Указывает на необходимость посылки подтверждения получения маршрута
        :param callback_required: Указывает на необходимость посылки клиенту URL-адреса ответной пересылки маршрута.
        :param expected_status: Ожидаемый статус ответа
        :return:
        """
        params = {"callbackRequired": callback_required} if callback_required else {}
        params.update({"targetEndpoint": target_endpoint, "deliveryAckRequired": delivery_ack_required})
        session.do_post(path=f"{self.base_path}/uploaded-routes", params=params, data=route,
                        expected_status=expected_status)
