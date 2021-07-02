from .common import CommonRouteExchangeService


class DataSubscriptions(CommonRouteExchangeService):
    """Класс для работы с данными подписок маршрутов"""

    def get_random_subscriptions_list(self, count):
        """Создание списка подпискичов
        :param count: Количество подписчиков
        """
        subs_list = []
        for _ in range(count):
            subs_list.append({
                'identityId': self.randomword(),
                'identityName': self.randomword(),
                'endpointURL': self.randomword()
            })
        return subs_list
