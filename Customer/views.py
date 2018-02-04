from django.http import HttpResponse,JsonResponse
from .models import Customer
from django.shortcuts import redirect
from  rest_framework.views import APIView
from  rest_framework.response import Response
from .serializers import CustomerSerializer
import pandas as pd
import numpy as np
from django.template import loader
from PythonScripts import regression
import matplotlib.pyplot as plt
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
        data = pd.read_csv('dataset.csv')
        data = np.array(data)
        x = data[:,1:7]
        for i in range(len(x)):
            if x[i][0] == user.customer_id:
                #print('Found')
                act_loan = x[i][3][1:-1]
                if act_loan == '' :
                    act_loan = 'None'

                refr = x[i][4][1:-1]
                if refr == '' :
                    refr = 'None'

                paid_loan = x[i][5][1:-1].split(', ')
                paid_loan = len(paid_loan)

                c = {
                    'user': user ,
                    'acc_bal' : x[i][1] ,
                    'fixed_dep' : x[i][2] ,
                    'active_loan' : act_loan ,
                    'refr' : refr ,
                    'paid_loan' : paid_loan ,
                }
                break;

        values , values_mmm = regression.start(user.customer_id)
        duration = [4, 8, 12]

        t = loader.get_template(os.path.dirname(os.path.dirname(__file__)) + '/Customer/Template/user_details.html')

        plt.plot(duration, values, c='b' , label='With Referees')
        plt.plot(duration, [values_mmm]*len(values), c='r', label='Without Referees')

        for i in range(len(values)):
            plt.text(duration[i]+0.1,values[i]-5000  ,str(i) + ' payment')

        plt.xlabel('Time (Months)')
        plt.ylabel('Loan Eligibility')
        plt.legend()
        address = 'Customer/static/Graphs/' + str(user.customer_id) + '-loan_graph.png'
        plt.savefig(address)
        return HttpResponse(t.render(c))



class GetUserJson(APIView):

    def get(self , request):
        id = request.GET['id']
        user = Customer.objects.get(customer_id=id)
        return JsonResponse({'user_id' : user.id ,
                             'user_name' : user.customer_name })


