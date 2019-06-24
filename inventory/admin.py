from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.forms import UserCreationForm, UserChangeForm


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'us_superuser', 'is_staff', 'is_activate')
    list_filter = ('is_superuser', 'is_staff', 'is_activate')
    fieldsets = [
        (None, {'fields': (
            'email',
            'password',
            'first_name',
            'last_name',
        )}),

        ('personal info', {'fields': (
            'credit_card',
            'city',
            'region',
            'postal_code',
            'country',
            'address_1',
            'addres_2',
            'shipping_region',
            'day_phone',
            'eve_phone',
            'mob_phone',
        )}),

        ('permissions', {'fields': ( 
            'groups',
            'user_permissions',
            'is_activate',
            'is_superuser',
            'is_staff',
        )}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    ]
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
