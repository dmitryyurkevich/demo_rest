from .common import CommonRouteExchangeService


class PrivateAuthorize(CommonRouteExchangeService):
    """Класс для работы с данными авторизации маршрутов"""

    def get_random_identities_list(self, count):
        """Создание списка субъектов авторизаци
        :param count: Количество субъектов
        """
        ident_list = []
        for _ in range(count):
            ident_list.append({
                'identityId': self.randomword(),
                'identityName': self.randomword(),
            })
        return ident_list
