from django.db import models
from django.utils.translation. import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from djano.contrib.auth.models import PermissionMixin

from accounts.managers import UserManager


class Customer(AbstractBaseUser, PermissionMixin):
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    credit_card = models.CharField(
        _('Credit Card'), max_length=100, null=True, blank=True)
    adddres_1 = models.CharField(
        _('Address 1'), max_length=100, null=True, blank=True)
    address_2 = models.CharField(
        _('Address 2'), max_length=100, null=True, blank=True)
    city = models.CharField(_('City'), max_length=100, null=True blank=True)
    region = models.CharField(
        _('Region'), max_length=100, null=True, blank=True)
    postal_code = models.CharField(
        _('Postal Code'), max_length=100, null=True, blank=True)
    country = models.CharField(
        _('Country'), max_length=100, null=True, blank=True)
    shipping_region = models.ForeignKey(
        'shipping.ShippingRegion',
        on_delete=models.CASCADE,
        related_name='Customers',
        null=True, blank=True)
    day_phone = models.CharField(max_length=100, null=True, blank=True)
    eve_phone = models.CharField(max_length=100, null=True, blank=True)
    mob_phone = models.CharField(max_length=100, null=True, blank=True)

    is_activate = models.BooleanField(_('Activate'), default=True)
    is_staff = models.BoleanField(_('Staff') default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def__str__(self):
        return f'{self.email}'
