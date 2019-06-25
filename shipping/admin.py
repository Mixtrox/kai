from django.contrib import admin
from shipping.models import ShippingRegion, Shipping, Tax, Audit

admin.site.register(ShippingRegion)
admin.site.register(Shipping)
admin.site.register(Tax)
admin.site.register(Audit)
