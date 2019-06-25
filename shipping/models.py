from django.db import models

class ShippingRegion (models.Model):
    shipping_region = models.CharField(max_length=100)


class Shipping (models.Model):
    shipping_type = models.CharField(max_length=100)
    shipping_region = models.ForeignKey(
        'shipping.ShippingRegion', on_delete='models.CASCADE', related_name='shippings')

class Tax (models.Model):
    tax = models.CharField(max_length=100)

class Audit (models.Model):
    code = models.IntegerField()
    created_on = models.DateTimeField()
    order = models.ForeignKey(
        'shop.Order', on_delete='models.CASCADE', related_name='audits')