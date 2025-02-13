from django.urls import path
from .views import edit_product

urlpatterns = [
    path("edit_product/<int:product_id>/", edit_product, name="edit_product")
]

