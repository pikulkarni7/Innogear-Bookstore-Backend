from django.contrib import admin
from .models import Customer, GoldCustomer, StoreItem, CartoonMovie, ComicBook, OrderLineItem, Order
# Register your models here.

admin.site.register(Customer)
admin.site.register(GoldCustomer)
admin.site.register(StoreItem)
admin.site.register(CartoonMovie)
admin.site.register(ComicBook)
admin.site.register(OrderLineItem)
admin.site.register(Order)
