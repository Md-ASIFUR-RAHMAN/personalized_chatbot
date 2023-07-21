from django.shortcuts import render, redirect,HttpResponse
import pandas as pd
from fuzzywuzzy import fuzz
from Home.views import *
from .models import *
import json,ast
import re
from Api.dataset_function import chatbot

import random
# Create your views here.

def Test(request):
    if request.method == "GET":

        return render(request, 'chatbot/test.html',)
    if request.method == "POST":

        ar_keys = []
        ar_values = []

        new_qs = []
        new_ans = []

        new_qs_data = []
        new_ans_data = []

        data = request.POST

        for i,j in data.items():
            ar_keys.append(i)
            ar_values.append(j)

        for k in range(1,len(ar_keys),2):
            new_qs.append(ar_keys[k])
            new_qs_data.append(ar_values[k])


        for k in range(2,len(ar_keys),2):
            new_ans.append(ar_keys[k])
            new_ans_data.append(ar_values[k])


        print(new_qs_data)
        print(new_ans_data)



        return HttpResponse('Ok')




def faq(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    if request.method == "GET":

        if ChatFaq.objects.filter(Idd=request.session['UserID']):
            pk = encode(request.session['UserID'])
            return redirect('chatbot:update',pk)

        name = reg.objects.get(ID = request.session['UserID'])
        context = {
            'name' : name
        }

        return render(request, 'chatbot/bot.html',context)

    if request.method=="POST":

        # qs1 = request.POST['qs1']
        # qs2 = request.POST['qs2']
        # qs3 = request.POST['qs3']
        # qs4 = request.POST['qs4']
        # qs5 = request.POST['qs5']
        #
        #
        # ans1 = request.POST['ans1']
        # ans2 = request.POST['ans2']
        # ans3 = request.POST['ans3']
        # ans4 = request.POST['ans4']
        # ans5 = request.POST['ans5']




        ar_keys = []
        ar_values = []

        new_qs = []
        new_ans = []

        new_qs_data = []
        new_ans_data = []

        data = request.POST


        data = data.dict()




        for i,j in data.items():
            ar_keys.append(i)
            ar_values.append(j)

        for k in range(1,len(ar_keys),2):
            new_qs.append(ar_keys[k])
            new_qs_data.append(ar_values[k])

        for k in range(2,len(ar_keys),2):
            new_ans.append(ar_keys[k])
            new_ans_data.append(ar_values[k])

        del data["csrfmiddlewaretoken"]

        # FAQ.objects.create(Idd = request.session['UserID'],qs1=qs1,qs2 = qs2, qs3 = qs3, qs4 = qs4, qs5 = qs5 , ans1 = ans1 , ans2 = ans2 , ans3 = ans3, ans4 = ans4, ans5 = ans5)

        ChatFaq.objects.create(Idd = request.session['UserID'],Question = new_qs_data ,Answer = new_ans_data, Dictionary = data)
        code = encode(request.session['UserID'])
        context = {
            'code' : code
        }
        return render(request,'chatbot/code.html',context)


def chat(request,action_id):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    df = pd.DataFrame()
    if request.method == "GET":

        return render(request, 'chatbot/chat_msg.html')

    if request.method=="POST":

        try:

            pk = decode(action_id)

            if ChatFaq.objects.filter(Idd = pk).first():

                msg = request.POST['msg']

                user = ChatFaq.objects.filter(Idd = pk).first()
                user_type = reg.objects.filter(ID=pk).first()

                # QS = [user.qs1,user.qs2,user.qs3,user.qs4,user.qs5]
                # ANS = [user.ans1,user.ans2,user.ans3,user.ans4,user.ans5]

                ini_list1 = user.Question
                ini_list2 = user.Answer


                res1 = ini_list1.strip('][').split(', ')
                res2 = ini_list2.strip('][').split(', ')

                print(res1)
                print(res2)


                df['Question'] = res1
                df['Answer'] = res2


                for i in range(len(df)):


                    f = fuzz.token_sort_ratio(msg, df['Question'][i])

                    if f >= 80.0:
                        # remove commas from end
                        val = df['Answer'][i].rstrip("\'")
                        # remove commas from start
                        val = val.lstrip("\'")
                        context = {
                            'idd' : pk,
                            'msg1': msg,
                            'msg' : val
                        }
                        return render(request,'chatbot/chat_msg.html',context)
                    else:
                        continue

                context = {
                    'idd': pk,
                    'msg1' : msg,
                    'msg' : chatbot(user_type.type,msg)

                }
                return render(request, 'chatbot/chat_msg.html', context)
            else:
                return HttpResponse("Chatbot not available")
        except:
            return HttpResponse("Chatbot is not valid format")


def update(request,pk):


    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    pk = decode(pk)
    if request.method == "GET":
        user = ChatFaq.objects.get(Idd=pk)

        data = user.Dictionary

        data = ast.literal_eval(data)

        print(data)

        ar_keys = []
        ar_values = []

        new_qs = []
        new_ans = []

        new_qs_data = []
        new_ans_data = []

        num = []


        for i,j in data.items():
            ar_keys.append(i)
            ar_values.append(j)

        for k in range(0,len(ar_keys),2):
            new_qs.append(ar_keys[k])
            new_qs_data.append(ar_values[k])


        for k in range(1,len(ar_keys),2):
            new_ans.append(ar_keys[k])
            new_ans_data.append(ar_values[k])

        pk = encode(pk)

        print(ar_keys)
        print(ar_values)

        print(new_qs)
        print(new_ans)

        user = zip(new_qs_data,new_ans_data)
        context = {
            'user': user,
            'user_api' : pk,
            'name' : request.session['UserName'],
        }
        return render(request, 'chatbot/update.html',context)

    if request.method == "POST":
        # qs1 = request.POST['qs1']
        # qs2 = request.POST['qs2']
        # qs3 = request.POST['qs3']
        # qs4 = request.POST['qs4']
        # qs5 = request.POST['qs5']
        #
        # ans1 = request.POST['ans1']
        # ans2 = request.POST['ans2']
        # ans3 = request.POST['ans3']
        # ans4 = request.POST['ans4']
        # ans5 = request.POST['ans5']



        # user = ChatFaq.objects.filter(Idd=pk)

        # for i in user:
        #     i.qs1 = qs1
        #     i.qs2 = qs2
        #     i.qs3 = qs3
        #     i.qs4 = qs4
        #     i.qs5 = qs5
        #
        #
        #     i.ans1 = ans1
        #     i.ans2 = ans2
        #     i.ans3 = ans3
        #     i.ans4 = ans4
        #     i.ans5 = ans5
        #
        #     i.save()


        user = ChatFaq.objects.get(Idd=pk)


        ar_keys = []
        ar_values = []

        new_qs = []
        new_ans = []

        new_qs_data = []
        new_ans_data = []

        data = request.POST
        data = data.dict()



        print(data)

        for i,j in data.items():

            print("key", i)
            print("val", j)

            ar_keys.append(i)
            ar_values.append(j)

        for k in range(1,len(ar_keys),2):
            new_qs.append(ar_keys[k])
            new_qs_data.append(ar_values[k])


        for k in range(2,len(ar_keys),2):
            new_ans.append(ar_keys[k])
            new_ans_data.append(ar_values[k])

        del data["csrfmiddlewaretoken"]

        print(ar_keys)
        print(ar_values)

        print(new_qs)
        print(new_ans)

        user.Question = new_qs_data
        user.Answer = new_ans_data
        user.Dictionary = data
        user.save()

        code = encode(pk)
        context = {
            'code': code
        }
        return render(request, 'chatbot/code.html', context)

def delete(request,pk):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    pk = decode(pk)
    user = ChatFaq.objects.get(Idd = pk)
    user.delete()
    return redirect('chatbot:faq')