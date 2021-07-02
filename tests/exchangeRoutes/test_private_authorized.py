import allure
import pytest

from tests import CommonTests


@allure.feature("Authorized - Private API")
class TestPrivateAuthorized(CommonTests):
    @allure.story("Добавление уникальных/дублирующих субъектов авторизации на маршрут (1 - нет дубликатов).")
    @pytest.mark.parametrize("duplicate", [1, 2])
    def test_add_unique_duplicate_authorized_identities(self, connection_route_1, res_test_data_identities, unique_uvid, duplicate):
        with allure.step("Step 1. Добавление субъектов авторизации на маршрут (с дубликатами и без)."):
            self.RES_PRIVATE_AUTHORIZE.add_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                authorized_identities=res_test_data_identities.idents_list * duplicate)

        with allure.step("Step 2. Запрос субъектов авторизации маршрута."):
            idents_list = self.RES_PRIVATE_AUTHORIZE.get_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 3. Проверка субъектов авторизации подписчика."):
            assert len(idents_list) == len(res_test_data_identities.idents_list), \
                "Количество субъектов авторизации не соответсвует ожидаемому."
            assert self.RES_ASSERTS_AUTHORIZE.is_sublist(received_list=idents_list,
                                                               expected_list=res_test_data_identities.idents_list), \
                "Искомые субъекты авторизации не найдены."

    @allure.story("Повторное добавление субъектов авторизации на маршрут.")
    def test_add_duplicate_authorized_identities(self, connection_route_1, res_test_data_identities, unique_uvid):
        with allure.step("Step 1. Добавление подписчика на маршрут."):
            self.RES_PRIVATE_AUTHORIZE.add_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                authorized_identities=res_test_data_identities.idents_list)

        with allure.step("Step 2. Повторное добавление того же подписчика на маршрут."):
            self.RES_PRIVATE_AUTHORIZE.add_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                authorized_identities=res_test_data_identities.idents_list)

        with allure.step("Step 3. Запрос субъектов авторизации маршрута."):
            idents_list = self.RES_PRIVATE_AUTHORIZE.get_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 4. Проверка субъектов авторизации подписчика."):
            assert len(idents_list) == len(res_test_data_identities.idents_list), \
                "Количество субъектов авторизации не соответсвует ожидаемому."
            assert self.RES_ASSERTS_AUTHORIZE.is_sublist(received_list=idents_list,
                                                               expected_list=res_test_data_identities.idents_list), \
                "Искомые субъекты авторизации не найдены."

    @allure.story("Изменение имени субъектов авторизации на маршруте.")
    def test_change_name_authorized_identities(self, connection_route_1, res_test_data_identities, unique_uvid):
        with allure.step("Step 1. Добавление субъектов авторизации на маршрут."):
            self.RES_PRIVATE_AUTHORIZE.add_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                authorized_identities=res_test_data_identities.idents_list)

        with allure.step("Step 2. Добавление субъектов авторизации с измененным Name на маршрут."):
            self.RES_PRIVATE_AUTHORIZE.add_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                authorized_identities=res_test_data_identities.idents_list_other_name)

        with allure.step("Step 3. Запрос субъектов авторизации маршрута."):
            idents_list = self.RES_PRIVATE_AUTHORIZE.get_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 3. Проверка субъектов авторизации подписчика."):
            assert len(idents_list) == len(res_test_data_identities.idents_list_other_name), \
                "Количество субъектов авторизации не соответсвует ожидаемому."
            assert self.RES_ASSERTS_AUTHORIZE.is_sublist(
                received_list=idents_list,
                expected_list=res_test_data_identities.idents_list_other_name), \
                "Искомые субъекты авторизации не найдены."

    @allure.story("Удаление субъектов авторизации.")
    @pytest.mark.parametrize("del_factor", [1, 2])
    def test_delete_authorized_identities(self, connection_route_1, res_test_data_identities, unique_uvid, del_factor):
        with allure.step("Step 1. Добавление субъектов авторизации на маршрут."):
            self.RES_PRIVATE_AUTHORIZE.add_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                authorized_identities=res_test_data_identities.idents_list)

        with allure.step("Step 2. Запрос субъектов авторизации маршрута."):
            idents_list = self.RES_PRIVATE_AUTHORIZE.get_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 3. Проверка количества субъектов авторизации."):
            idents_len = len(res_test_data_identities.idents_list)
            assert len(idents_list) == idents_len, "Количество субъектов авторизации не соответсвует ожидаемому."

        with allure.step("Step 4. Удаление субъектов авторизации."):
            self.RES_PRIVATE_AUTHORIZE.del_authorized_identities_from_uvid(
                session=connection_route_1,
                uvid=unique_uvid,
                authorized_identities=res_test_data_identities.idents_list[:idents_len // del_factor])

        with allure.step("Step 5. Запрос субъектов авторизации маршрута."):
            idents_list = self.RES_PRIVATE_AUTHORIZE.get_authorized_identities_from_route_by_uvid(
                session=connection_route_1,
                uvid=unique_uvid)

        with allure.step("Step 6. Проверка субъектов авторизации маршрута."):
            assert len(idents_list) == idents_len - idents_len // del_factor, \
                "Количество субъектов авторизации не соответсвует ожидаемому."
            assert self.RES_ASSERTS_AUTHORIZE.is_sublist(
                received_list=idents_list,
                expected_list=res_test_data_identities.idents_list[idents_len // del_factor:]), \
                "Искомые субъекты авторизации не найдены."
