from library.application.route_exchange_service.common import Common


class PublicAcknowledgements(Common):
    """Класс для работы с публичным API маршрутов"""

    def __init__(self):
        self.uri = f'{Common.public_api_uri}/published-routes'

    def post_acknowledgements(self, session, delivery_ack, expected_status=Common.HTTPStatus.NO_CONTENT):
        """Принимает подтверждение от клиента, что маршрут клиентом принят.
        :param session: Сессия сервиса
        :param delivery_ack: Подтверждение принятия маршрута.
        :param expected_status: Ожидаемый статус ответа
        """
        session.do_post(path=self.uri, data=delivery_ack, expected_status=expected_status)
