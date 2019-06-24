from django.db import models

class Customer (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    address_1 =  models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    day_phone = models.CharField(max_length=100)
    eve_phone = models.CharField(max_length=100)
    mob_phone = models.CharField(max_length=100)
    shipping_region = models.ForeignKey(
        'shipping.Shipping_Region', on_delete='models.CASCADE', related_name='customers')

