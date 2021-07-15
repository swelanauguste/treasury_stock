from django.contrib import admin
from .models import Category, Product, Supplier


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Supplier)