from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductModel
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from utils.make_woocommerce_request import make_woocommerce_request

# @@OK TODO: Implement view for getting all the products from the database
def get_all_products(request):
    products = ProductModel.objects.all().values()
    return JsonResponse(list(products), safe=False)

# @@OK TODO: Implement view for editing a product in the database
@csrf_exempt
@require_http_methods(["POST"])
def edit_product(request, product_id):
    try:
        product = ProductModel.objects.get(id=product_id)
        data = json.loads(request.body)
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.description = data.get('description', product.description)
        product.save()
        edit_product_woocommerce(product)
        return JsonResponse({'message': 'ProductModel updated successfully'})
    except ProductModel.DoesNotExist:
        return JsonResponse({'error': 'ProductModel not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

def edit_product_woocommerce(product):
    data_product = {
        "name": product.name,
    }
    product_edited = make_woocommerce_request(f'products/{product.external_id}?force=true', 'PUT', data_product)