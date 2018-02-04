from django.http import HttpResponse,JsonResponse
from .models import Customer
from django.shortcuts import redirect
from  rest_framework.views import APIView
from  rest_framework.response import Response
from .serializers import CustomerSerializer
from django.template import loader
#import matplotlib.pyplot as plt
import os

# Create your views here.

#predict/
class CustomerList(APIView) :

    def get(self , request):
        customer = Customer.objects.all()

        serializer = CustomerSerializer(customer , many=True)
        return Response(serializer.data)



class CheckLogin(APIView):

    def post(self, request):
        id = request.POST.get("id" , "")
        password = request.POST.get("pass" , "")
        customer = Customer.objects.filter(customer_id=id).filter(customer_password=password).values()
        html = ""
        if len(customer) > 0:
            user = Customer.objects.get(customer_id=id)
            request.session['customer_id'] = str(user.customer_id)
            return redirect('user_panel')
        else:
            html = "<html><body>Incorrect Credentials</body></html>"
            return HttpResponse(html)


class UserPanel(APIView):

    def get(self , request):
        print(request)
        user = Customer.objects.get(customer_id=request.session['customer_id'])
        t = loader.get_template(os.path.dirname(os.path.dirname(__file__)) + '/Customer/Template/user_details.html')
        c = {
            'user': user
        }
        #plt.plot([1, 2, 3], [5, 10, 11], c='b')
        #plt.xlabel('Time')
        #plt.ylabel('Reputation')
        address = 'Customer/static/Graphs/' + str(user.customer_id) + '-loan_graph.png'
        #plt.savefig(address)
        return HttpResponse(t.render(c))    



class GetUserJson(APIView):

    def get(self , request):
        id = request.GET['id']
        user = Customer.objects.get(customer_id=id)
        return JsonResponse({'user_id' : user.id ,
                             'user_name' : user.customer_name })


