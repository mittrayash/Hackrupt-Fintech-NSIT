from django.http import HttpResponse
from django.http import Http404
from .models import Customer
from django.shortcuts import render , get_object_or_404
from  rest_framework.views import APIView
from  rest_framework.response import Response
from  rest_framework import status
from .serializers import CustomerSerializer

# Create your views here.

# List all artists or create a new one
#predict/
class CustomerList(APIView) :

    def get(self , request):
        id = 0
        #id = request.GET['id']
        if id == 0 :
            artist = Customer.objects.all()
        else:
            artist = Customer.objects.filter(customer_id=id).values()
        serializer = CustomerSerializer(artist , many=True)
        return Response(serializer.data)