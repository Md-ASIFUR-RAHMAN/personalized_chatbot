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


class ChatAPI(APIView):


    def post(self, request,id):

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