import random
import string
import uuid


class Common:
    """Общий класс"""
    ROUTE_MAPPING_STATUS = [
        {"id": 1, "name": "ORIGINAL"},
        {"id": 2, "name": "PLANNED_FOR_VOYAGE"},
        {"id": 3, "name": "OPTIMIZED"},
        {"id": 4, "name": "CROSS_CHECKED"},
        {"id": 5, "name": "SAFETY_CHECKED"},
        {"id": 6, "name": "APPROVED"},
        {"id": 7, "name": "USED_FOR_MONITORING"},
        {"id": 8, "name": "INACTIVE"}
    ]

    def randomword(self, length=10):
        """Генерация сучайного набора букв
        :param length: Длина набора букв
        :return: Набор букв
        """
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for _ in range(length))

    def generate_uvid(self):
        """Генерация UVID
        :return: UVID
        """
        return f"urn:mrn:ksnb:voyage:uvid:{self.randomword(4)}:{uuid.uuid4()}"

    def read_file(self, path):
        """Открытие и чтение файла
        :param path: Путь до файла
        :return:
        """
        with open(path, "r") as f:
            return f.read()
