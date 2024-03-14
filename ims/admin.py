from django.contrib import admin
from .models import Customer, Product, Stock, Order, Supplier

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
  list_display = ("customer_name", "address", "phone")

class ProductAdmin(admin.ModelAdmin):
  list_display = ("item_code", "item_name", "price","tin_size")

class OrderAdmin(admin.ModelAdmin):
  list_display = ("product", "customer", "quantity","status","created_at","processed_at")


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock)
admin.site.register(Order, OrderAdmin)
admin.site.register(Supplier)