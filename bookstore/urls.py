from django.urls import path


from .views import create_customer



app_name = 'bookstore'

urlpatterns = [
     path('bookstore/createcustomer/', create_customer),
]