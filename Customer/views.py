from django.http import HttpResponse
from django.http import Http404
from .models import Customer
from django.shortcuts import render,redirect
from  rest_framework.views import APIView
from  rest_framework.response import Response
from  rest_framework import status
from .serializers import CustomerSerializer
from django.template import Context, loader
import os

# Create your views here.

# List all artists or create a new one
#predict/
class CustomerList(APIView) :

    def get(self , request):
        customer = Customer.objects.all()

        serializer = CustomerSerializer(customer , many=True)
        return Response(serializer.data)



class CheckLogin(APIView):

    def getHtml(self , user):
        html = "<html><body> User Id : " + str(user.id) + "<br>User Account : " + str(user.customer_id) + "<br>User Name : " + str(user.customer_name) + "</body></html>"
        return html


    def get(self, request):
        id = request.GET['id']
        password = request.GET['pass']
        customer = Customer.objects.filter(customer_id=id).filter(customer_password=password).values()
        html = ""
        if len(customer) > 0 :
            user = Customer.objects.get(customer_id=id)

            t = loader.get_template(os.path.dirname(os.path.dirname( __file__ ))+'/Customer/Template/userdetails.html')
            c = {
                'user': user
            }
            return HttpResponse(t.render(c))
        else :
            html = "<html><body>Incorrect Credentials</body></html>"
            return HttpResponse(html)





class UserPage(APIView):

    def get(self , request):
        print(request)
        html = "<html><body>User Page</body></html>"
        return HttpResponse(html)





