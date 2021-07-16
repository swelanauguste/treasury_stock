from django.contrib import admin
from .models import Category, Product, Supplier, ReceiveGood, DeliveryGood


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'qty', 'get_total_quantity']


admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(ReceiveGood)
admin.site.register(DeliveryGood)
