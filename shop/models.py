from django.db import models


class Department (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Category (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(
        'shop.Department', on_delete=models.CASCADE, related_name='categories')


class ShoppingCart (models.Model):
    attributes = models.TextField()
    quantity = models.IntegerField()
    buy_now = models.IntegerField(default=true)
    added_on = models.DateTimeField()
    product = models.ForeignKey(
        'inventory.Product', on_delete=models.CASCADE, related_name='shoppingcarts')
    cart = models.TextField()    


class Order (models.Model):
    comments = models.CharField(max_length=255)
    auth_code = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(default=0)
    created_on = models.DateTimeField()
    shipped_on = models.DateTimeField()
    customer = models.ForeignKey(
      'accounts.Customer',  on_delete=models.CASCADE, related_name='orders')
    shipping = models.ForeignKey(
        'shipping.Shipping', on_delete=models.CASCADE, related_name='orders')  
    tax = models.ForeignKey(
        'shipping.Tax', on_delete=models.CASCADE, related_name='orders')    


class OrderDetail (models.Model):
    product_name = models.CharField(max_length=100)
    attributes = models.TextField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(
        'shop.Order', on_delete='models.CASCADE', related_name='order_details')
    product = models.ForeignKey(
        'inventory.Product', on_delete='models.CASCADE', related_name='order_details')    


class Review (models.Model):
    rating = models.IntegerField()
    created_on = models.DateTimeField()
    customer = models.ForeignKey(
        'accounts.Customer', on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(
        'inventory.Product', on_delete=models.CASCADE, related_name='reviews')    

