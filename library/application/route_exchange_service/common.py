from http import HTTPStatus


class Common:
    """Общий класс"""

    res_private_api_uri = "/res/api/v1/private"
    public_api_uri = "/res/api/v1/public"
    headers_xml = {"Content-Type": "application/xml"}
    headers_json = {"Content-Type": "application/json"}
    HTTPStatus = HTTPStatus
