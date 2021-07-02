from http import HTTPStatus


class Common:
    """Общий класс"""

    vts_route_api_uri = '/vts-route-service/api/v1/'
    headers_xml = {'Content-Type': 'application/xml'}
    headers_json = {'Content-Type': 'application/json'}
    HTTPStatus = HTTPStatus
