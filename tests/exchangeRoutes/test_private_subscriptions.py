
import allure
import pytest

from tests import CommonTests


@allure.feature("Subscriptions - Private API")
class TestPrivateSubscriptions(CommonTests):
    @allure.story("Добавление уникальных/дублирующих подписчиков на него (1 - нет дубликатов).")
    @pytest.mark.parametrize("duplicate", [1, 2])
    def test_add_unique_duplicate_subscriptions(self, connection_route_1, res_test_data_subscription, unique_uvid, duplicate):
        with allure.step("Step 1. Добавление подписчика на маршрут (с дубликатами и без)."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list * duplicate)

        with allure.step("Step 2. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 3. Проверка идентификатора подписчика."):
            assert len(subs_list) == len(res_test_data_subscription.subscriptions_list), "Количество подписчиков не соответсвует ожидаемому."
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=subs_list,
                expected_list=res_test_data_subscription.subscriptions_list), \
                "Искомый подписчик не найден."

    @allure.story("Добавление комбинации уникальных и дублирующих подписчиков на него.")
    def test_add_combination_unique_duplicate_subscriptions(self, connection_route_1, res_test_data_subscription, unique_uvid):
        with allure.step("Step 1. Добавление комбинированных подписчиков на маршрут."):
            add_subs_list = res_test_data_subscription.subscriptions_list * 2 + res_test_data_subscription.subscriptions_list_other
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=add_subs_list)

        with allure.step("Step 2. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 3. Проверка идентификатора подписчика."):
            assert len(subs_list) == len(res_test_data_subscription.subscriptions_list) + len(res_test_data_subscription.subscriptions_list_other), \
                "Количество подписчиков не соответсвует ожидаемому."
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(received_list=subs_list,
                                                                   expected_list=add_subs_list), \
                "Искомый подписчик не найден."

    @allure.story("Повторное добавление подписчиков на него.")
    def test_add_duplicate_subscriptions(self, connection_route_1, res_test_data_subscription, unique_uvid):
        with allure.step("Step 1. Добавление подписчика на маршрут."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list)

        with allure.step("Step 2. Повторное добавление того же подписчика на маршрут."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list)

        with allure.step("Step 3. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 4. Проверка идентификатора подписчика."):
            assert len(subs_list) == len(res_test_data_subscription.subscriptions_list), \
                "Количество подписчиков не соответсвует ожидаемому."
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=subs_list,
                expected_list=res_test_data_subscription.subscriptions_list), \
                "Искомый подписчик не найден."

    @allure.story("Добавление подписчикa с таким же ID/Name и другим EndPointUrl.")
    def test_add_subscriptions_with_other_url(self, connection_route_1, res_test_data_subscription, unique_uvid):
        with allure.step("Step 1. Добавление подписчика на маршрут."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list)

        with allure.step("Step 2. Добавление подписчика с измененным endpointURL на маршрут."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list_other_url)

        with allure.step("Step 3. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 4. Проверка идентификатора подписчика."):
            expected_list = res_test_data_subscription.subscriptions_list + res_test_data_subscription.subscriptions_list_other_url
            assert len(subs_list) == len(expected_list), \
                "Количество подписчиков не соответсвует ожидаемому."
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=subs_list,
                expected_list=expected_list), \
                "Искомый подписчик не найден."

    @allure.story("Изменение имени подписчикa.")
    def test_change_name_subscriptions(self, connection_route_1, res_test_data_subscription, unique_uvid):
        with allure.step("Step 1. Добавление подписчика на маршрут."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list)

        with allure.step("Step 2. Добавление подписчика с измененным Name на маршрут."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list_other_name)

        with allure.step("Step 3. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 4. Проверка идентификатора подписчика."):
            assert len(subs_list) == len(res_test_data_subscription.subscriptions_list_other_name), \
                "Количество подписчиков не соответсвует ожидаемому."
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=subs_list,
                expected_list=res_test_data_subscription.subscriptions_list_other_name), \
                "Искомый подписчик не найден."

    @allure.story("Удаление подписчиков.")
    @pytest.mark.parametrize("del_factor", [1, 2])
    def test_delete_subscriptions(self, connection_route_1, res_test_data_subscription, unique_uvid, del_factor):
        with allure.step("Step 1. Добавление подписчика на маршрут."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list)

        with allure.step("Step 2. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 3. Проверка количества подписчиков."):
            subs_len = len(res_test_data_subscription.subscriptions_list)
            assert len(subs_list) == subs_len, "Количество подписчиков не соответсвует ожидаемому."

        with allure.step("Step 4. Удаление подписчиков"):
            self.RES_PRIVATE_SUBSCRIPTIONS.del_subscriptions_from_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list[:subs_len // del_factor])

        with allure.step("Step 5. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 6. Проверка идентификатора подписчика."):
            assert len(subs_list) == subs_len - subs_len // del_factor, \
                "Количество подписчиков не соответсвует ожидаемому."
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=subs_list,
                expected_list=res_test_data_subscription.subscriptions_list[subs_len // del_factor:]), \
                "Искомый подписчик не найден."

    @allure.story("Удаление несуществующих подписчиков.")
    def test_delete_not_exist_subscriptions(self, connection_route_1, res_test_data_subscription, unique_uvid):
        with allure.step("Step 1. Добавление подписчика на маршрут."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list)

        with allure.step("Step 2. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 3. Проверка количества подписчиков."):
            assert len(subs_list) == len(res_test_data_subscription.subscriptions_list), \
                "Количество подписчиков не соответсвует ожидаемому."

        with allure.step("Step 4. Удаление несуществующих подписчиков"):
            self.RES_PRIVATE_SUBSCRIPTIONS.del_subscriptions_from_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list_other)

        with allure.step("Step 5. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 6. Проверка идентификатора подписчика."):
            assert len(subs_list) == len(res_test_data_subscription.subscriptions_list), \
                "Количество подписчиков не соответсвует ожидаемому."
            assert self.RES_ASSERTS_SUBSCRIPTIONS.is_sublist(
                received_list=subs_list,
                expected_list=res_test_data_subscription.subscriptions_list), \
                "Искомый подписчик не найден."

    @allure.story("Удаление комбинированного списка существующих/несуществующих подписчиков.")
    def test_delete_combination_not_exist_subscriptions(self, connection_route_1, res_test_data_subscription, unique_uvid):
        with allure.step("Step 1. Добавление подписчика на маршрут."):
            self.RES_PRIVATE_SUBSCRIPTIONS.add_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list)

        with allure.step("Step 2. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 3. Проверка количества подписчиков."):
            assert len(subs_list) == len(res_test_data_subscription.subscriptions_list), \
                "Количество подписчиков не соответсвует ожидаемому."

        with allure.step("Step 4. Удаление комбинированного списка сущестующих/несуществующих подписчиков"):
            self.RES_PRIVATE_SUBSCRIPTIONS.del_subscriptions_from_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                subs_list=res_test_data_subscription.subscriptions_list + res_test_data_subscription.subscriptions_list_other)

        with allure.step("Step 5. Запрос подписчиков маршрута."):
            subs_list = self.RES_PRIVATE_SUBSCRIPTIONS.get_subscriptions_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 6. Проверка идентификатора подписчика."):
            assert len(subs_list) == 0, "Количество подписчиков не соответсвует ожидаемому."
