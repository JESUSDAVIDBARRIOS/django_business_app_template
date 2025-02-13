from django.db import models

class ClientModel(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)

    @classmethod
    def get_or_create_from_billing(cls, billing_info):
        client, created = cls.objects.get_or_create(
            name=billing_info['first_name']+' '+billing_info['last_name'],
            email=billing_info['email'],
            phone=billing_info['phone']
        )
        return client

    def __str__(self):
        return self.name
    
class AddressModel(models.Model):
    
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    @classmethod
    def get_or_create_from_shipping(cls, shipping_info):
        address, created = cls.objects.get_or_create(
            address=shipping_info['address_1']+' '+shipping_info['address_2'],
            city=shipping_info['city'],
            state=shipping_info['state'],
            country=shipping_info['country']
        )
        return address
    def __str__(self):
        return self.address