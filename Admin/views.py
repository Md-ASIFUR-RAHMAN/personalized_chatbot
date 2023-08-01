from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

# Create your views here.
from django.views.decorators.csrf import csrf_protect
from chatbot.models import ChatFaq
from Home.models import *
from payment.models import *
from chatbot.models import *

import hashlib
import hashlib

import requests
from django.shortcuts import render,redirect,HttpResponse
# from .models import Registration as reg
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

def Dashboard(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "ADMIN":
        return redirect('Admin:Login')
    admin_name = "ADMIN"
    if "AdminName" in request.session:
        admin_name = request.session["AdminName"]
    context = {
        'admin_name': admin_name,
        'all_user_count': Registration.objects.count(),
        'total_chatbot_user': ChatFaq.objects.count(),
        'paid_user': payment_info.objects.filter(Status='ok').count(),
        'trial_user': Trial.objects.filter(Status='on').count()
    }
    return render(request, 'admin/dashboard.html', context)


@csrf_protect
def Login(request):

    if request.method == 'POST':
        # Login user
        data = request.POST
        print(data)
        email = data['username']
        password = data['password']

        if email == "asifur15-13196@diu.edu.bd" and password == "alex100":
            request.session['VisitorStatus'] = 'ADMIN'
            request.session["AdminID"] = '1'
            request.session["AdminName"] = 'ayon'

            return redirect('Admin:Dashboard')
        else:
            return redirect('Admin:Login')


        # exists = UserAccount.objects.filter(email=email).exists()


        # if not exists:
            # show message ('This admin does not exist')
        #     print('This admin does not exist')
        #     return redirect('Admin:Login')
        # admin = UserAccount.objects.get(email=email)

        # if not 'ADMIN' in admin.get_role_list():
        #     print('Access Denied')
        #     return redirect('Admin:Login')
        # if admin.password != password:
        #     # show message ('Wrong Password. Please Check Again')
        #     print('Wrong Password. Please Check Again')
        #     return redirect('Admin:Login')

        # request.session['VisitorStatus'] = admin.role
        # request.session["AdminID"] = admin.id
        # request.session["AdminName"] = admin.name
        #
        # return redirect('Admin:Dashboard')
    else:
        request.session['current_page'] = 'AdminLogin'

        context = {

        }
        return render(request, 'admin/login.html', context)

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

def Add_Member(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "ADMIN":
        return redirect('Admin:Login')

    if request.method == 'POST':
        # Login user
        data = request.POST
        if Registration.objects.filter(Phone = data['phone']).exists():
            context = {
                'msg' : "Phone number already exist"
            }
            return render(request, 'admin/user/add_member.html', context)

        title_name = data['name'].replace(' ', '_')
        img_new_name = title_name + '.jpg'

        name = data['name']
        email = data['email']
        phone = data['phone']
        gender = data['gender']
        passw = data['passw']
        # repassw = data['repassw']
        password = hashlib.md5(passw.encode('utf-8')).hexdigest()

        new_member = Registration(Name=name, Phone=phone, Email=email, Gender=gender, Password=password, pro_pic=img_new_name)
        new_member.save()

        user = Registration.objects.get(Email=email)
        f_name = user.ID
        image_compress_save(request.FILES['picture'], img_new_name, str(f_name))

        return redirect('Admin:Show_Member')
    else:
        request.session['current_page'] = 'AdminLogin'

        context = {

        }
        return render(request, 'admin/user/add_member.html', context)

def Show_Member(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "ADMIN":
        return redirect('Admin:Login')

    request.session['current_page'] = 'Show Members'

    members = Registration.objects.all()

    context = {
        'members': members
    }
    return render(request, 'admin/user/show_member.html', context)

# @csrf_protect
def Edit_Member(request, member_id):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "ADMIN":
        return redirect('Admin:Login')

    if request.method == 'POST':
        member = Registration.objects.get(ID=int(member_id))
        print(member)
        data = request.POST


        if request.FILES.get('picture') != None:
            member_name = data['name'].replace(' ', '_')
            img_new_name = member_name+'_'+data['phone']+'.jpg'
            image_compress_save(request.FILES['picture'], img_new_name,member_id)

            print(img_new_name)
            member.pro_pic = img_new_name
            member.Name = data['name']
            member.Phone = data['phone']
            member.Email = data['email']
            member.Gender = data['gender']


        else:

            member.Name = data['name']
            member.Phone = data['phone']
            member.Email = data['email']
            member.Gender = data['gender']
            member.pro_pic = member.pro_pic
            member.save()
        # path = default_storage.save('tmp/somename.mp3', ContentFile(data.read()))
        # tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        context = {
            'member_id': member_id,
            'member': member,
        }
        return render(request, 'admin/user/edit_member.html', context)

    else:
        # Login user
        print(member_id)
        request.session['current_page'] = 'Edit Member Admin'
        member = Registration.objects.get(pk=int(member_id))

        if member.Phone.startswith('88'):
            member.Phone = member.Phone[2:]
        elif member.Phone.startswith('+88'):
            member.Phone = member.Phone[3:]
        context = {
            'member_id': member_id,
            'member': member,
        }
        print(member.Name)
    return render(request, 'admin/user/edit_member.html', context)


def Delete_Member(request, member_id):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "ADMIN":
        return redirect('Admin:Login')


    Registration.objects.filter(pk=int(member_id)).delete()

    print(member_id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def Show_chat_Member(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "ADMIN":
        return redirect('Admin:Login')

    request.session['current_page'] = 'Show Members'

    members = payment_info.objects.all()

    context = {
        'members': members
    }
    return render(request, 'admin/user/show_chat_member.html', context)