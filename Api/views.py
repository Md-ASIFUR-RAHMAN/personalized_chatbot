from urllib import request

from django.shortcuts import render
from rest_framework import status

from .serializer import *
# import jwt, datetime , string
from rest_framework.views import APIView
from rest_framework.response import Response
from chatbot.views import *
import pandas as pd
from Api.dataset_function import chatbot
from Api.prediction_dataset import chatbot_new
from Home.models import Registration as reg
# Create your views here.
from chatbot.models import Trial
from datetime import datetime, timedelta
from payment.models import payment_info


def basic(pk):
    try:
        idd = pk
        print(idd)
        user = Trial.objects.get(Idd=idd)
        new_date = datetime.today().date()
        print(user.datee)
        print(new_date)
        new = new_date - user.datee
        print(new.days)

        if new.days > 3:
            print(new.days)

            user.Status = 'over'
            user.save()

            return 'over'

        # elif user.Status == 'off':
        #
        #     return 'off'

        else:
            return 'on'
    except:
        return 'on'

def advance(pk):
    try:
        idd = pk
        print(idd)
        user = payment_info.objects.get(buyer_id=idd)
        new_date = datetime.today().date()
        print(user.buy_date)
        print(new_date)

        new = new_date - user.buy_date
        print(new.days)

        if new.days > 3:
            print(new.days)

            user.Status = 'over'
            user.save()

            return 'over'
        else:
            return 'ok'
    except:
        return 'on'


class ChatAPI(APIView):


    def post(self, request,id):
        pk = decode(id)

        if advance(pk) == 'over':
            return Response(
                {
                    'message': 'Chatbot 1 month Subscription is over'

                }, status=status.HTTP_200_OK
            )
        elif advance(pk) == 'ok':
            df = pd.DataFrame()

            pk = decode(id)

            if ChatFaq.objects.filter(Idd=pk).first():

                data = request.data
                print(data)

                msg = request.data['message']

                user = ChatFaq.objects.filter(Idd=pk).first()
                user_type = reg.objects.filter(ID=pk).first()

                ini_list1 = user.Question
                ini_list2 = user.Answer

                res1 = ini_list1.strip('][').split(', ')
                res2 = ini_list2.strip('][').split(', ')

                df['Question'] = res1
                df['Answer'] = res2

                for i in range(len(df)):

                    f = fuzz.token_sort_ratio(msg, df['Question'][i])

                    if f >= 80.0:
                        # remove commas from end
                        val = df['Answer'][i].rstrip("\'")
                        # remove commas from start
                        val = val.lstrip("\'")

                        return Response(
                            {
                                'message': val

                            }, status=status.HTTP_200_OK
                        )

                    else:
                        continue

                return Response(
                    {
                        'message': chatbot(user_type.type, msg)

                    }, status=status.HTTP_200_OK
                )
            else:

                return Response(
                    {
                        'message': 'Chatbot Not Available'

                    }, status=status.HTTP_200_OK
                )

        elif basic(pk) == 'over' and advance(pk) == 'over' :
            return Response(
                {
                    'message': 'Chatbot Subscription is over'

                }, status=status.HTTP_200_OK
            )

        elif basic(pk) == 'over':
            return Response(
                {
                    'message': 'Chatbot Trial Subscription is over'

                }, status=status.HTTP_200_OK
            )

        #############

        df = pd.DataFrame()

        pk = decode(id)

        if ChatFaq.objects.filter(Idd = pk).first():

            data = request.data
            print(data)

            msg = request.data['message']

            user = ChatFaq.objects.filter(Idd = pk).first()
            user_type = reg.objects.filter(ID = pk).first()


            ini_list1 = user.Question
            ini_list2 = user.Answer


            res1 = ini_list1.strip('][').split(', ')
            res2 = ini_list2.strip('][').split(', ')


            df['Question'] = res1
            df['Answer'] = res2


            for i in range(len(df)):


                f = fuzz.token_sort_ratio(msg, df['Question'][i])

                if f >= 80.0:
                    # remove commas from end
                    val = df['Answer'][i].rstrip("\'")
                    # remove commas from start
                    val = val.lstrip("\'")

                    return Response(
                        {
                            'message': val

                        }, status=status.HTTP_200_OK
                    )

                else:
                    continue

            return Response(
                {
                    'message': chatbot(user_type.type,msg)

                }, status=status.HTTP_200_OK
            )
        else:

            return Response(
                {
                    'message': 'Chatbot Not Available'

                }, status=status.HTTP_200_OK
            )