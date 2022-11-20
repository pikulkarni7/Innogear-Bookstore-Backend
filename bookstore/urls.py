from django.urls import path


from .views import create_customer, create_order_line_item, compute_order_total



app_name = 'bookstore'

urlpatterns = [
     path('bookstore/createcustomer/', create_customer),
     path('bookstore/createorderlineitem/', create_order_line_item),
     path('bookstore/computetotal/', compute_order_total)
]