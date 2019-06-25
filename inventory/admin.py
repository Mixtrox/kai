from django.contrib import admin
from inventory.models import Product, Attribute, AttributeValue

admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
