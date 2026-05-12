from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from cart.models import Cart,CartItem
from orders.models import Order,OrderItem


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    # Formulaire d'édition
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {'fields': ('phone', 'address')}),
    )

    # Formulaire d'ajout
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations supplémentaires', {'fields': ('email', 'phone', 'address')}),
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('id','user','session_key')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display=('cart','product','quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','user','shipping_address','is_paid','created_at')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=('order','product','quantity','price')