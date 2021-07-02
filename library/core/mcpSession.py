import functools
import requests

from json import JSONDecodeError
from urllib3 import disable_warnings, exceptions

from httpHelper import do_request, get_payload


MCP_TOKEN_REQUEST_URL = ""
MCP_TEST_PASS = "idreg-admin"

disable_warnings(exceptions.InsecureRequestWarning)


def reauthorize_on_401(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        response = method(self, *args, **kwargs)
        if response.status_code == 401:
            self.authorize()
            response = method(self, *args, **kwargs)
        return response
    return wrapper


class McpSession(requests.Session):
    def __init__(self):
        super().__init__()
        self.customize().authorize().ignore_ssl()

    def customize(self):
        self.headers["accept"] = "application/json;charset=UTF-8"
        return self

    def ignore_ssl(self):
        self.verify = False
        return self

    def authorize(self):
        self.headers["Authorization"] = f"Bearer {get_mcp_access_token()}"
        return self

    @reauthorize_on_401
    def do_get(self, url, **kwargs):
        return do_request(method=self.get, url=url, **kwargs)

    @reauthorize_on_401
    def do_post(self, url, **kwargs):
        return do_request(method=self.post, url=url, **kwargs)

    @reauthorize_on_401
    def do_patch(self, url, **kwargs):
        return do_request(method=self.patch, url=url, **kwargs)

    @reauthorize_on_401
    def do_delete(self, url, **kwargs):
        return do_request(method=self.delete, url=url, **kwargs)


def get_mcp_access_token():
    url = MCP_TOKEN_REQUEST_URL
    data = get_payload(grant_type="password", client_id="setupclient", username=MCP_TEST_USER, password=MCP_TEST_PASS)
    response = do_request(method="post", url=url, data=data, verify=False)
    try:
        mcp_access_token = response.json()["access_token"]
        print("a new mcp access token received")
        return mcp_access_token
    except (JSONDecodeError, KeyError,) as e:
        raise RuntimeError(f"can not get mcp access token:\n{e}")


if __name__ == "__main__":
    org = 123
    agent = 456

    with McpSession() as mcp_session:
        mcp_session.do_get(url=f"https://api.mcp-test.maritimecloud.net/oidc/api/org/{org}/agent/{agent}")
