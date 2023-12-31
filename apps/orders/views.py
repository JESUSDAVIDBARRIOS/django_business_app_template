from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.make_woocommerce_request import make_woocommerce_request

from .models import OrderModel

@api_view(["GET"])
def route_index(request):
    """Returns a list of all available routes.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """
    routes = [
        "get_orders_woocommerce",
        "get_local_orders"
    ]
    return Response(routes)

@api_view(["GET"])
def get_orders_woocommerce(request):
    """Gets all orders from the WooCommerce API and creates them in the database.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """
    # TODO: Make a request to the WooCommerce API to get all orders and create them in the database.
    # The creation of the orders should include OrderModel, OrderItemModel, ClientModel and AddressModel objects.
    # The method make_woocommerce_request would be useful for making the request to the WooCommerce API.
    # Use the endpoint 'orders' to get all orders from WooCommerce.
    return Response({})

@api_view(["GET"])
def get_local_orders(request):
    """Gets all orders from the database.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """
    # TODO: Create a serializer for the OrderModel and return the serialized data.
    # The serializer should include the OrderModel, OrderItemModel, ClientModel and AddressModel objects.
    return Response({})
