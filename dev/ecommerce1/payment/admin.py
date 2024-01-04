from django.contrib import admin

from . models import ShippingAddress, Order, OrderItem

# admin.site.register(ShippingAddress)

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "address1", "city"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "amount_paid", "date_ordered"]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price", "user"]
    

