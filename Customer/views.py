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
        id = request.GET['id']
        if id == 0 :
            customer = Customer.objects.all()
        else:
            customer = Customer.objects.filter(customer_id=id).values()

        serializer = CustomerSerializer(customer , many=True)
        return Response(serializer.data)



class CheckLogin(APIView):

    def get(self, request):
        id = request.GET['id']
        password = request.GET['pass']
        customer = Customer.objects.filter(customer_id=id).values()
        html = ""
        if len(customer) > 0 :
            html = "<html><body>Login Success</body></html>"
        else :
            html = "<html><body>Incorrect Credentials</body></html>"

        return HttpResponse(html)