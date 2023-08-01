import hashlib

import requests
from django.shortcuts import render,redirect,HttpResponse
from .models import Registration as reg
from PIL import Image
from django.core.files import File
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from io import BytesIO
import os
import random
import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import auth

def test(request):
    return render(request,'Home/test_chat.html')
def test_another(request):
    return render(request,'Home/test_chat2.html')

def About(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    return render(request,'Home/about.html')

# Create your views here.
def image_compress_save(image, img_name,f_name):
    im = Image.open(image)  # or self.files['image'] in your form
    # destroy color pew pew
    im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    compressed_image = File(im_io, name=img_name)
    print(settings.STATIC_URL)
    print(settings.STATIC_ROOT)
    print(settings.STATICFILES_DIRS[0])
    FileSystemStorage(location=os.path.join(settings.STATICFILES_DIRS[0], 'UPLOAD', 'NewUser',f_name)).save(img_name,
                                                                                                    compressed_image)
def listToString(s):

    str1 = ""

    for ele in s:
        str1 += ele

    return str1

def encode(pk):
    j = random.randint(1001, 9999)
    code = 'Chatbotapi' + str(j) + str(pk)
    return code

def decode(pk):
    code = list(pk)
    pk = code[14:]
    return listToString(pk)

def send_simple_message(request):

    if request.method == 'GET':

        return render(request,'Home/forgot_password.html')


    if request.method == 'POST':

        data = request.POST

        if reg.objects.filter(Email = data['email']):

            otp = random.randint(1000 , 9999)
            user_obj = reg.objects.get(Email = data['email'])
            user_obj.OTP = otp
            user_obj.save()


            # Define email sender and receiver
            email_sender = 'ayonssolution@gmail.com'
            email_password = 'sexbmaxiqtzhyylp'
            email_receiver = data['email']

            # Set the subject and body of the email
            subject = 'Recover Password'
            body = """
                This is your OTP {}
            """.format(otp)

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            # Add SSL (layer of security)
            context = ssl.create_default_context()

            # Log in and send the email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            return redirect('Home:verify',user_obj.ID)
        else:
            return HttpResponse('not ok')


def verify(request,action_id):

    if request.method == 'GET':

        user = reg.objects.get(ID = action_id)
        context = {
            'user' : user
        }
        return render(request,'Home/verify.html',context)

    if request.method == 'POST':

        data = request.POST

        user = reg.objects.get(ID=action_id)

        if data['verify'] == user.OTP:

            # return HttpResponse('ok')
            return redirect('Home:Recover',user.ID)
        else:
            context = {
                'msg' : 'wrong otp',
                'user': user
            }
            return render(request, 'Home/verify.html',context)


def Recover(request,action_id):

    if request.method == 'GET':
        user = reg.objects.get(ID=action_id)
        context = {
            'user': user
        }
        return render(request, 'Home/recover.html', context)

    if request.method == 'POST':

        data = request.POST

        user = reg.objects.get(ID=action_id)

        if data['pass1'] == data['pass2']:
            password = hashlib.md5(data['pass1'].encode('utf-8')).hexdigest()
            user.Password = password
            user.save()

            return redirect('Home:Login')
        else:
            context = {
                'msg': 'your password does not matched',
                'user': user
            }
            return render(request, 'Home/recover.html', context)

def home(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    return render(request,'Home/index.html')

def home2(request):
    return render(request,'Home/index2.html')

def Dashboard(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    return render(request,'Home/index.html')


def Services(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    return render(request,'Home/services.html')



def Profile(request):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    try:
        id = request.session['UserID']

        print(id)


        user =  reg.objects.get(ID=id)

        print(user.Name)
        context= {
            'user' : user
        }
        return render(request,'Home/profile.html',context)
    except:
        return redirect('Home:Login')



def Profile_Pic_Edit(request,action_id):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')


    user = reg.objects.get(ID=action_id)

    if request.method == 'GET':

        context= {
            'user' : user
        }
        return render(request,'Home/profile_pic_edit.html',context)

    if request.method == 'POST':

        try:
            os.remove('static/UPLOAD/NewUser/{}/{}'.format(str(action_id),user.pro_pic))
        except:
            pass

        name = user.Name

        title_name = name.replace(' ', '_')
        img_new_name = title_name + '_new' + '.jpg'
        image_compress_save(request.FILES['picture'], img_new_name,str(action_id))

        user.pro_pic = img_new_name
        user.save()


        return redirect('Home:Profile')


def Profile_Info_Edit(request,action_id):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    user = reg.objects.get(ID=action_id)

    if request.method == 'GET':

        context= {
            'user' : user
        }
        return render(request,'Home/profile_info_edit.html',context)

    if request.method == 'POST':

        data = request.POST

        password = hashlib.md5(data['passw'].encode('utf-8')).hexdigest()


        user.Name= data['name']
        user.Email= data['email']
        user.Phone = data['phone']
        user.Gender = data['gender']
        user.type = data['type']
        user.Password = password
        user.save()


        return redirect('Home:Profile')




@csrf_protect
def Login(request):

    if request.method == 'GET':
        return render(request, 'Home/login.html')

    if request.method == 'POST':
        # Login user
        data = request.POST
        email = data['email']

        password = hashlib.md5(data['passw'].encode('utf-8')).hexdigest()
        exists = reg.objects.filter(Email=email).exists()

        if not exists:
            context = {
                'msg': "Wrong Email"
            }

            return render(request, 'Home/login.html', context)

            # show message ('This Member does not exist')
            # return redirect('Home:Login')

        user = reg.objects.get(Email=email)
        if user.Password != password:
            # show message ('Wrong Password. Please Check Again')
            # return redirect('Home:Login')

            context = {
                'msg' : "Wrong Password"
            }

            return render(request,'Home/login.html',context)
        else:

            # Login Successfull

            request.session['VisitorStatus'] = 'user'
            request.session["UserID"] = user.ID
            request.session["UserName"] = user.Name

            user.last_login = datetime.now()
            user.save()

            idd = user.ID
            idd = encode(idd)

            return redirect('Home:Dashboard')


@csrf_protect
def Registration(request):

    if request.method == 'GET':
        return render(request,'Home/reg.html')

    if request.method == 'POST':
        # Register user
        data = request.POST

        name = data['name']
        email = data['email']
        phone = data['phone']
        gender = data['gender']
        passw = data['passw']
        repassw = data['repassw']
        chatbot_type = data['typee']



        if reg.objects.filter(Email=email).exists():
            # show flash message later

            context = {
                'msg1' : "This Email Already Exist"
            }

            return render(request,'Home/reg.html',context)

        elif reg.objects.filter(Phone=phone).exists():
            # show flash message later
            context = {
                'msg2' : "This Phone Number Already Exist"
            }

            return render(request,'Home/reg.html',context)

        elif passw == repassw:
            password = hashlib.md5(passw.encode('utf-8')).hexdigest()

            title_name =data['name'].replace(' ', '_')
            img_new_name = title_name+'.jpg'

            new_member = reg(Name=name, Phone=phone, Email=email, Gender=gender,Password=password, pro_pic = img_new_name,type=chatbot_type)
            new_member.save()

            user = reg.objects.get(Email = email)
            f_name = user.ID
            image_compress_save(request.FILES['picture'], img_new_name,str(f_name))


            # show flash success message
            return redirect('Home:Login')

        elif passw != repassw:
            context = {
                'msg3' : "Both Password are not matched"
            }

            return render(request,'Home/reg.html',context)

def Logout(request):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    try:
        del request.session['VisitorStatus']
        del request.session["UserID"]
        del request.session["UserName"]
        return redirect('Home:Login')

    except:
        return redirect('Home:Login')

