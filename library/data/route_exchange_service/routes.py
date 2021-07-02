import os
import xml.etree.ElementTree as Et
import copy

from .common import CommonRouteExchangeService


class DataRoutes(CommonRouteExchangeService):
    """Класс для работы с данными аршрутов"""

    def get_route_from_file(self, path_route):
        """Считывание маршрута из файла
        :param path_route: Путь до маршрута в формате XML
        :return: ElementTree
        """
        path_file = os.path.join(os.getcwd(), path_route)
        return Et.parse(path_file)

    def change_uvid_in_route(self, tree_route, uvid):
        """Замена UVID в маршруте
        :param tree_route: Маршрут в формате XML
        :param uvid: UVID
        :return: ElementTree
        """
        tree_route_copy = copy.deepcopy(tree_route)
        root = tree_route_copy.getroot()
        root.find('.//*[@vesselVoyage]').attrib.update({'vesselVoyage': uvid})
        return tree_route_copy

    def change_status_in_route(self, tree_route, status):
        """Замена статуса маршрута в маршруте
        :param tree_route: Маршрут в формате XML
        :param status: Cтатус маршрута 1 - ORIGINAL
                                       2 - PLANNED_FOR_VOYAGE
                                       3 - OPTIMIZED
                                       4 - CROSS_CHECKED
                                       5 - SAFETY_CHECKED
                                       6 - APPROVED
                                       7 - USED_FOR_MONITORING
                                       8 - INACTIVE
        :return: ElementTree
        """
        tree_route_copy = copy.deepcopy(tree_route)
        root = tree_route_copy.getroot()
        root.find('.//*[@routeStatus]').attrib.update({'routeStatus': str(status)})
        return tree_route_copy

    def change_route_name_in_route(self, tree_route, route_name):
        """Замена routeName в маршруте
        :param tree_route: Маршрут в формате XML
        :param route_name: Имя маршрута
        :return: ElementTree
        """
        tree_route_copy = copy.deepcopy(tree_route)
        root = tree_route_copy.getroot()
        root.find('.//*[@routeName]').attrib.update({'routeName': route_name})
        return tree_route_copy

    def convert_route_to_str(self, tree_route):
        return Et.tostring(tree_route.getroot(), encoding='UTF-8')