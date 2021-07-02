from library.application.route_exchange_service.common import Common


class PrivateServiceInstances(Common):
    """Класс для работы с приватным API запросов к экземплярам сервисов"""

    def __init__(self):
        self.base_path = f"{Common.res_private_api_uri}/service-instances"

    def search(self, session, fields=None, page=None, size=None, sort=None, filter=None,
               expected_status=Common.HTTPStatus.OK):
        """
        :param session: Сессия сервиса
        :param fields: Список запрашиваемых полей.
        :param page: Порядковый номер запрашиваемой страницы результатов
        :param size: Размер страницы
        :param sort: Размер страницы
        :param filter: Критерии сортировки в формате: property(,asc|desc).
        :param expected_status: Ожидаемый статус ответа
        :return: Список сервисов
        """
        params = {"fields": fields} if fields else {}
        params.update({"page": page} if page else {})
        params.update({"size": size} if size else {})
        params.update({"sort": sort} if sort else {})
        data = {"filter": filter} if filter else {}

        return session.do_post(path=f"{self.base_path}/search", params=params, data=data,
                               expected_status=expected_status).json()
