import json
from http import HTTPStatus

import requests

from library.application.route_exchange_service.common import Common


class PrivateSubscriptions(Common):
    """Класс для работы с приватным API подписок маршрутов"""

    def __init__(self):
        self.uri = f"{Common.res_private_api_uri}/subscriptions"

    def get_subscriptions_from_route_by_uvid(self, session, uvid):
        """Получение подписчиков маршрута
        :param session: Сессия сервиса
        :param uvid: Идентификатор маршрута
        :return: Список подписчиков маршрута
        """
        params = {"uvid": uvid}
        response = session.do_get(path=self.uri, params=params, headers=Common.headers_json)
        return response.json()

    def add_subscriptions_from_route_by_uvid(self, session, uvid, subs_list):
        """Добавление подписчика на маршрут
        :param session: Сессия сервиса
        :param uvid: Идентификатор маршрута
        :param subs_list: Список подписчиков
        """
        params = {"uvid": uvid}
        return session.do_post(path=self.uri, params=params, data=json.dumps(subs_list),
                               headers=Common.headers_json, expected_status=Common.HTTPStatus.NO_CONTENT)

    def del_subscriptions_from_uvid(self, session, uvid, subs_list):
        """Удаление подписчиков с маршрута
        :param session: Сессия сервиса
        :param uvid: Идентификатор маршрута
        :param subs_list: Список подписчиков
        """
        params = {"uvid": uvid}
        return session.do_delete(path=self.uri, params=params, data=json.dumps(subs_list),
                                 headers=Common.headers_json, expected_status=Common.HTTPStatus.NO_CONTENT)
