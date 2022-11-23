from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
import random

from .queries import addCustomer, createOrderLineItem, computeTotal, createCustomerOrder



@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny,])
def create_customer(request):
    if request.method == 'POST':
        try:
            name=request.data['name']
            type=request.data['type']
            email=request.data['email']
            address=request.data['address']
            id = random.randint(1000, 5000)            
            addCustomer(id=id, type=type, email=email, address=address, name=name)            
            return Response({"message" : "Customer created"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"message": "Faield to create order"}, status=status.HTTP_400_BAD_REQUEST) 



@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny,])
def create_customer_order(request):
    if request.method == 'POST':
        try:
            order_id = createCustomerOrder(customerid=request.data['customer_id'])
            for item in request.data['items']:            
                itemid=item['itemid']
                copies_ordered=item['copies']
                createOrderLineItem(itemid=itemid, orderid=order_id, copies_ordered=copies_ordered)
            return Response({"message" : "Created order", "order_id": order_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"message": "Failed to create order"}, status=status.HTTP_400_BAD_REQUEST) 



@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny,])
def compute_order_total(request):
    if request.method == 'POST':
        try:
            order_id=request.data['orderid']
            total = computeTotal(orderid=order_id)        
            return Response({"message" : total}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"message": "Faield to compute total"}, status=status.HTTP_400_BAD_REQUEST)
        