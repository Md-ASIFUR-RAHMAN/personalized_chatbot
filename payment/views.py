import datetime

from django.shortcuts import render,HttpResponse
from .models import *
from Home.views import encode, decode
# Create your views here.






# def success(request):

def getapi(request):

    try :
        user = payment_info.objects.get(buyer_id=request.session['UserID'])

        if user.Status == 'ok':
            code = encode(request.session['UserID'])
            context = {
                'code': code
            }
            return render(request, 'chatbot/code_api.html', context)

    except:

        if request.method == 'GET':
            return render(request,'payment/get_bill_info.html')

        if request.method == 'POST':

            data =  request.POST
            # user = payment_info.objects.get(buyer_id = request.session['UserID'])

            if data['amount'] == '500.0' and len(data['cardNumber']) == 8:

                date = datetime.datetime.now()

                payment_info.objects.create(Status = 'ok',CardNumber = data['cardNumber'],CardName = data['cardName'],ExpiryDate = data['expiryDate'],buyer_name = request.session['UserName'] , buyer_id = request.session['UserID']  , amount = data['amount'] , buy_date = date)

                code = encode(request.session['UserID'])
                context = {
                    'code': code
                }
                return render(request,'chatbot/code_api.html',context)

            else:
                context = {
                    'msg' : 'Card is not valid'
                }
                return render(request, 'payment/get_bill_info.html',context)
