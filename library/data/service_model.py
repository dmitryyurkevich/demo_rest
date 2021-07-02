from .common import Common


class ServiceModel(Common):
    """Класс для работы с моделями данных сервисов"""

    def create_vessle_info(self, vessel_name=None, vessel_imo=None, vessel_mmsi=None):
        """Модель данных краткая справка о судне (VesselInfo)
        :param vessel_name: Имя судна
        :param vessel_imo: Номер международной морской организации (International Maritime Organization) судна
        :param vessel_mmsi: Идентификатор морской подвижной службы (Maritime Mobile Service Identity) судна
        :return: Справка о судне
        """
        return {
            "name": vessel_name,
            "vesselId": {
                "imo": vessel_imo,
                "mmsi": vessel_mmsi
            }
        }

    def create_route_dto(self, route_id=None, route_name=None, route_rtz=None, route_status=None, uvid=None,
                         vessel_name=None, vessel_imo=None, vessel_mmsi=None):
        """Модель данных краткая справка о маршруте, вместе с содержимым маршрута (RouteDTO)
        :param route_id: Идентификатор маршрута
        :param route_name: Наименование маршрута
        :param route_rtz: Маршрут в RTZ формате
        :param route_status: Статус маршрута
        :param uvid: UVID маршрута
        :param vessel_name: Имя судна
        :param vessel_imo: Номер международной морской организации (International Maritime Organization) судна
        :param vessel_mmsi: Идентификатор морской подвижной службы (Maritime Mobile Service Identity) судна
        :return: Маршрут
        """
        return {
            "id": route_id,
            "name": route_name,
            "rtz": route_rtz,
            "status": route_status,
            "uvid": uvid,
            "vesselInfo": self.create_vessle_info(vessel_name=vessel_name, vessel_imo=vessel_imo,
                                                  vessel_mmsi=vessel_mmsi)
        }

    def create_exchange_route_dto(self, exchange_route_id=None, service_mrn=None, state=None, version=None,
                                  date_received=None, date_sent=None, date_updated=None, route_id=None, route_name=None,
                                  route_rtz=None, route_status=None, uvid=None, vessel_name=None, vessel_imo=None,
                                  vessel_mmsi=None):
        """Модель данных обменного маршрута (exchangeRouteDTO)
        :param exchange_route_id: Идентификатор обменного маршрута
        :param service_mrn: MRN сервиса, связанного с обменным маршрутом
        :param state: Состояние обмена маршрута
        :param version: Версия
        :param date_received: Дата получения маршрута от субъекта
        :param date_sent: Дата отправки маршрута субъекту
        :param date_updated: Дата последнего обновления маршрута
        :param route_id: Идентификатор маршрута
        :param route_name: Наименование маршрута
        :param route_rtz: Маршрут в RTZ формате
        :param route_status: Статус маршрута
        :param uvid: UVID маршрута
        :param vessel_name: Имя судна
        :param vessel_imo: Номер международной морской организации (International Maritime Organization) судна
        :param vessel_mmsi: Идентификатор морской подвижной службы (Maritime Mobile Service Identity) судна
        :return: Обменный маршрут
        """
        return {
            "id": exchange_route_id,
            "received": date_received,
            "route": self.create_route_dto(route_id=route_id, route_name=route_name, route_rtz=route_rtz,
                                           route_status=route_status, uvid=uvid, vessel_name=vessel_name,
                                           vessel_imo=vessel_imo, vessel_mmsi=vessel_mmsi),
            "sent": date_sent,
            "serviceMRN": service_mrn,
            "state": state,
            "updated": date_updated,
            "version": version
        }
