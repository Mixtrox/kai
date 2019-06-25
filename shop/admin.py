from django.contrib import admin
from shop.models import Department, Category, ShoppingCart, Order, OrderDetail, Review


admin.site.register(Department)
admin.site.register(Category)
admin.site.register(ShoppingCart)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Review)
