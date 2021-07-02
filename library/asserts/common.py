def is_sublist(received_list, expected_list):
    """Проверка вхождения списка в список
    :param received_list: Список в который должен входить список
    :param expected_list: Ожидаемый список
    :return: Результат проверки
    """
    return set(received_list) <= set(expected_list)
