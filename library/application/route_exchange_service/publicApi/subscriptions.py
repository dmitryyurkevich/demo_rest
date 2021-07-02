from library.application.route_exchange_service.common import Common


class PublicSubscriptions(Common):
    """Класс для работы с публичным API подписчиков"""

    def __init__(self):
        self.uri = f'{Common.public_api_uri}/subscriptions'

    def get_subscriptions(self, session, callback_endpoint, expected_status=Common.HTTPStatus.OK):
        """Возвращает список UVID, на которые подписан подписчик.
        :param session: Сессия сервиса
        :param callback_endpoint: URL-адрес подписчика
        :param expected_status: Ожидаемый статус ответа
        :return: Список UVID
        """
        params = {'callbackEndpoint ': callback_endpoint}
        return session.do_get(path=self.uri, params=params, expected_status=expected_status).json()

    def post_subscriptions(self, session, callback_endpoint, uvid=None, expected_status=Common.HTTPStatus.NO_CONTENT):
        """Регистрирует подписчика маршрутов.
        :param session: Сессия сервиса
        :param callback_endpoint: URL-адрес подписчика
        :param uvid: Идентификатор маршрута
        :param expected_status: Ожидаемый статус ответа
        """
        params = {'callbackEndpoint ': callback_endpoint}
        params.update({'uvid': uvid} if uvid else {})
        session.do_post(path=self.uri, params=params, expected_status=expected_status)

    def del_subscriptions(self, session, callback_endpoint, uvid=None, expected_status=Common.HTTPStatus.NO_CONTENT):
        """Возвращает список UVID, на которые подписан подписчик.
        :param session: Сессия сервиса
        :param callback_endpoint: URL-адрес подписчика
        :param uvid: Идентификатор маршрута
        :param expected_status: Ожидаемый статус ответа
        """
        params = {'callbackEndpoint ': callback_endpoint}
        params.update({'uvid': uvid} if uvid else {})
        session.do_delete(path=self.uri, params=params, expected_status=expected_status)
