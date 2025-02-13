from django.db import models

from apps.clients.models import ClientModel, AddressModel
from apps.products.models import ProductModel

class OrderModel(models.Model):

    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    external_id = models.CharField(max_length=100)

    def __str__(self):
        return self.client.name

class OrderItemModel(models.Model):

    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    # TODO: Add a foreign key to the ProductModel.