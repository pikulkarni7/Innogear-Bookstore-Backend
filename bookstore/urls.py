from django.urls import path


from .views import create_customer, create_customer_order, compute_order_total, make_gold_customer



app_name = 'bookstore'

urlpatterns = [
     path('bookstore/createcustomer/', create_customer),
     path('bookstore/createcustomerorder/', create_customer_order),
     path('bookstore/computetotal/', compute_order_total),
     path('bookstore/makegold/', make_gold_customer)
]