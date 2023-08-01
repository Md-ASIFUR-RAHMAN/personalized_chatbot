import datetime

from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *
from Home.views import encode, decode
# Create your views here.
from chatbot.models import Trial
from datetime import datetime, timedelta
from .check import gateway


# def success(request):

def getapi_withpay(request):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

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
            return render(request,'payment/payment_plan.html')


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

def getapi_trial(request):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    if request.method == 'POST':

        try:
            Trial.objects.create(Idd = request.session['UserID'],Status = 'on', datee=datetime.today().date())
            code = encode(request.session['UserID'])
            context = {
                'code': code
            }
            return render(request, 'chatbot/code_api.html', context)

        except:
            context ={
                'message_trial' : 'you already use trial mode'
            }
            return render(request, 'payment/payment_plan2.html',context)


def getapi_advance(request):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    try :
        user = payment_info.objects.get(buyer_id=request.session['UserID'])
        print(1)
        if user.Status == 'ok':
            code = encode(request.session['UserID'])
            context = {
                'code': code
            }
            return render(request, 'chatbot/code_api.html', context)

        else:
            if request.method == 'GET':
                print(2)

                if payment_info.objects.get(buyer_id=request.session['UserID']):
                    user = payment_info.objects.get(buyer_id=request.session['UserID'])
                    user.delete()

                return render(request, 'payment/get_bill_info.html')

            if request.method == 'POST':

                data = request.POST
                # user = payment_info.objects.get(buyer_id = request.session['UserID'])

                if data['amount'] == '1800.0' and len(data['cardNumber']) == 8:

                    date = datetime.today().now()

                    payment_info.objects.create(Status='ok', CardNumber=data['cardNumber'], CardName=data['cardName'],
                                                ExpiryDate=data['expiryDate'], buyer_name=request.session['UserName'],
                                                buyer_id=request.session['UserID'], amount=data['amount'],
                                                buy_date=date)

                    user = Trial.objects.get(Idd=request.session['UserID'])
                    user.Status = 'over'
                    user.save()

                    code = encode(request.session['UserID'])
                    context = {
                        'code': code
                    }
                    return render(request, 'chatbot/code_api.html', context)

                else:
                    context = {
                        'msg': 'Card is not valid'
                    }
                    return render(request, 'payment/get_bill_info.html', context)

    except:

        if request.method == 'GET':
            print(2)

            # if payment_info.objects.get(buyer_id = request.session['UserID']):
            #     user = payment_info.objects.get(buyer_id = request.session['UserID'])
            #     user.delete()

            return render(request,'payment/get_bill_info.html')


        if request.method == 'POST':

            data =  request.POST
            # user = payment_info.objects.get(buyer_id = request.session['UserID'])

            if data['amount'] == '1800.0' and len(data['cardNumber']) == 8:

                date = datetime.today().now()

                payment_info.objects.create(Status = 'ok',CardNumber = data['cardNumber'],CardName = data['cardName'],ExpiryDate = data['expiryDate'],buyer_name = request.session['UserName'] , buyer_id = request.session['UserID']  , amount = data['amount'] , buy_date = date)

                # user = Trial.objects.get(Idd=request.session['UserID'])
                # user.Status = 'over'
                # user.save()

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


def getapi_pro(request):
    if request.method == 'POST':
        return render(request, 'payment/get_bill_info.html')

def ssl(request):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    val = gateway('Ayonsolution','Ayonsolution@gmail.com')
    print(val['sessionkey'])

    return HttpResponseRedirect(val['GatewayPageURL'])


def paymentt(request):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    try:
        idd = request.session['UserID']
        user = Trial.objects.get(Idd=idd)

        if user.Status == 'over':
            return render(request, 'payment/payment_plan2.html')
        else:
            return render(request, 'payment/payment_plan2.html')


    except:

        return render(request, 'payment/payment_plan.html')


@csrf_exempt
def success(request):

    context = {
        'message': 'Payment Successful'
    }
    return render(request, 'payment/success.html', context)

def get_Api(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    code = encode(request.session['UserID'])
    context = {
        'code': code
    }
    return render(request, 'chatbot/code_api.html', context)

@csrf_exempt
def fail(request):

    return redirect('payment:paymentt')