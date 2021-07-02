import json

from library.application.route_exchange_service.common import Common


class PrivateAuthorize(Common):
    """Класс для работы с приватным API авторизации"""

    def __init__(self):
        self.uri = f"{Common.res_private_api_uri}/authorized-identities"

    def get_authorized_identities_from_route_by_uvid(self, session, uvid):
        """Получение список субъектов, которым разрешена подписка на маршрут
        :param session: Сессия сервиса
        :param uvid: Идентификатор маршрута
        :return: Список субъектов
        """
        params = {"uvid": uvid}
        response = session.do_get(path=self.uri, params=params, headers=Common.headers_json)
        return response.json()

    def add_authorized_identities_from_route_by_uvid(self, session, uvid, authorized_identities):
        """Добавление субъектов в список субъектов, которым разрешена подписка на маршрут
        :param session: Сессия сервиса
        :param uvid: Идентификатор маршрута
        :param authorized_identities: Список субъектов
        """
        params = {"uvid": uvid}
        return session.do_post(path=self.uri, params=params, data=json.dumps(authorized_identities),
                               headers=Common.headers_json, expected_status=Common.HTTPStatus.NO_CONTENT)

    def del_authorized_identities_from_uvid(self, session, uvid, authorized_identities):
        """Удаление подписчиков с маршрута
        :param uvid: Идентификатор маршрута
        :param authorized_identities: Список субъектов
        """
        params = {"uvid": uvid}
        return session.do_delete(path=self.uri, params=params, data=json.dumps(authorized_identities),
                                 headers=Common.headers_json, expected_status=Common.HTTPStatus.NO_CONTENT)
