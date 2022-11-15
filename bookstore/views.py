from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
import random
from . import forms
from .queries import addCustomer
# Create your views here.


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny,])
def create_customer(request):
    if request.method == 'POST':
        name=request.data['name']
        type=request.data['type']
        email=request.data['email']
        address=request.data['address']
        id = random.randint(1000, 5000)
        
        addCustomer(id=id, type=type, email=email, address=address, name=name)
        
        return Response({"message" : "tujya aichi gand"}, status=status.HTTP_201_CREATED)
        
        
    return None