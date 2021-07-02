from library import application, asserts, data


class CommonTests:
    """List of all the APIs under the test"""

    # Route Exchange Service
    RES_PRIVATE_ROUTES = application.route_exchange_service.pivateApi.PrivateRoutes()
    RES_PRIVATE_AUTHORIZE = application.route_exchange_service.pivateApi.PrivateAuthorize()
    RES_PRIVATE_SUBSCRIPTIONS = application.route_exchange_service.pivateApi.PrivateSubscriptions()

    RES_PUBLIC_ROUTES = application.route_exchange_service.publicApi.PublicRoutes()

    RES_ASSERTS_AUTHORIZE = asserts.route_exchange_service.AssertsAuthorize()
    RES_ASSERTS_SUBSCRIPTIONS = asserts.route_exchange_service.AssertsSubscriptions()

    RES_DATA_ROUTES = data.route_exchange_service.DataRoutes()
    RES_DATA_AUTHORIZE = data.route_exchange_service.PrivateAuthorize()
    RES_DATA_SUBSCRIPTIONS = data.route_exchange_service.DataSubscriptions()
