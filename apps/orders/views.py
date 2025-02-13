from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.make_woocommerce_request import make_woocommerce_request

from .models import OrderModel, OrderItemModel
from .serializers import OrderModelSerializer, OrderItemModelSerializer
from apps.clients.models import ClientModel, AddressModel

from apps.products.models import ProductModel
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
    orders = make_woocommerce_request('orders', 'GET')
    for obj_order in orders:

        client = ClientModel.get_or_create_from_billing(obj_order['billing'])
        print(client)
        
        address = AddressModel.get_or_create_from_shipping(obj_order['shipping'])
        
        order = OrderModel.objects.filter(external_id=obj_order['id']).first()
        if not order:
            order = OrderModel.objects.create(
                client=client,
                address=address,
                total=obj_order['total'],
                status=obj_order['status'],
                external_id=obj_order['id'])
        
        for obj_item in obj_order['line_items']:
            product = ProductModel.objects.filter(external_id=obj_item['id']).first()
            if not product:
                product = ProductModel.objects.create(
                    name=obj_item['name'],
                    description=obj_item['name'],
                    price=obj_item['price'],
                    stock=100,
                    external_id=obj_item['product_id'])

            order_item = OrderItemModel.objects.filter(order=order, product=product).first()
            if not order_item:
                order_item = OrderItemModel.objects.create(
                quantity=obj_item['quantity'],
                unit_price=obj_item['price'],
                order=order,
                product=product)

    return Response(orders)

@api_view(["GET"])
def get_local_orders(request):
    orders = OrderModel.objects.all()
    orders_serialized = OrderModelSerializer(orders, many=True)
    return Response(orders_serialized.data)
