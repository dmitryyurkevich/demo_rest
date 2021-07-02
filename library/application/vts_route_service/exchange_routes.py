from library.application.vts_route_service.common import Common


class ExchangeRoutes(Common):
    """Класс для работы с API маршрутов"""

    def __init__(self):
        self.uri = f'{Common.vts_route_api_uri}/exchange-routes'

    def search_exchange_routes(self, session, service_mrn=None, mmsi=None, imo=None,  route_name=None, fields=None,
                               expected_status=Common.HTTPStatus.OK):
        """Поиск информации об обменных маршрутах сервиса или судна.
        :param session: Сессия сервиса
        :param service_mrn: MRN сервиса
        :param mmsi: MMSI судна
        :param imo: IMO судна
        :param route_name: Имя маршрута
        :param fields: Список полей для фильрации (['id', 'route.id'])
        :param expected_status: Ожидаемый статус ответа
        :return: список обменных маршрутов
        """
        params = {'serviceMRN': service_mrn} if service_mrn else {}
        params.update({'mmsi': mmsi} if mmsi else {})
        params.update({'imo': imo} if imo else {})
        params.update({'routeName': route_name} if route_name else {})
        params.update({'fields': ','.join(fields)} if fields else {})

        return session.do_get(path=self.uri, params=params, expected_status=expected_status).json()

    def get_exchange_routes(self, session, exchange_route_id, expected_status=Common.HTTPStatus.OK):
        """Получение информации об обменном маршруте по ID.
        :param session: Сессия сервиса
        :param exchange_route_id: Идентификатор обменного маршрута
        :param expected_status: Ожидаемый статус ответа
        :return: Информация по обменноу маршруту
        """
        return session.do_get(path=f'{self.uri}/{exchange_route_id}', expected_status=expected_status).json()

    def get_services(self, session, mmsi=None, imo=None, expected_status=Common.HTTPStatus.OK):
        """Получение информации об обменном маршруте по ID.
        :param session: Сессия сервиса
        :param mmsi: MMSI судна
        :param imo: IMO судна
        :param expected_status: Ожидаемый статус ответа
        :return: Информация по обменноу маршруту
        """
        params = {'mmsi': mmsi} if mmsi else {}
        params.update({'imo': imo} if imo else {})
        return session.do_get(path=f'{self.uri}/services', expected_status=expected_status).json()

    def post_exchange_routes(self, session, exchange_route_dto, expected_status=Common.HTTPStatus.OK):
        """Создание нового обменного маршрута.
        :param session: Сессия сервиса
        :param exchange_route_dto: модель данных exchangeRouteDTO
        :param expected_status: Ожидаемый статус ответа
        :return: Информация по обменноу маршруту
        """
        return session.do_post(path=self.uri, data=exchange_route_dto, expected_status=expected_status).json()

    def send_exchange_routes(self):
        """API на этапе реализации"""
        pass

    def put_exchange_routes(self, session, exchange_route_id, exchange_route_dto,
                            expected_status=Common.HTTPStatus.NO_CONTENT):
        """Обновление обменного маршрута.
        :param session: Сессия сервиса
        :param exchange_route_id: Идентификатор обменного маршрута
        :param exchange_route_dto: модель данных exchangeRouteDTO
        :param expected_status: Ожидаемый статус ответа
        """
        session.do_post(path=f'{self.uri}/{exchange_route_id}', data=exchange_route_dto,
                        expected_status=expected_status)
