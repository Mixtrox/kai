from django.db import models


class Product (models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=150)
    image_2 = models.CharField(max_length=150)
    thumbnail = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    display = models.IntegerField(default=0)
    categories = models.ManyToManyField(
        'shop.Category', related_name='products')
    attributes = models.ManyToManyField(
        'inventory.AttributeValue', related_name='products')


class Attribute (models.Model):
    name = models.CharField(max_length=100)


class AttributeValue (models.Model):
    value = models.CharField(max_length=100)
    Attribute = models.ForeignKey(
        'inventory.Attribute', on_delete='models.CASCADE', related_name='attribute_values')
