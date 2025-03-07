from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'tipo', 'created_at', 'updated_at']
    list_filter = ['tipo', 'created_at', 'updated_at']
    search_fields = ['name', 'tipo']
    list_per_page = 10
