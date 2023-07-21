from django.shortcuts import render,redirect
import pyqrcode
import wget
# from PIL import Image
from django.core.files import File
from django.conf import settings
from io import BytesIO
from django.core.files.storage import FileSystemStorage
# import png
import os
from pyqrcode import QRCode

# Create your views here.

def remove_png_from_static_folder(idd):

    static_folder_path = 'static/UPLOAD/qrimg/{}/'.format(idd)  # Replace with the actual path to your static folder

    for filename in os.listdir(static_folder_path):
        file_path = os.path.join(static_folder_path, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('.png')):
            os.remove(file_path)

def Generate_QR(request):

    # String which represents the QR code

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    if request.method == 'GET':
        return render(request,'QR/generate_qr.html')

    if request.method == 'POST':

        # s = input(""" """)

        data = request.POST

        val = data['value']

        url = pyqrcode.create("""{}""".format(val))

        url.png('static/UPLOAD/qrimg/{}.png'.format((request.session['UserName'])), scale=6)

        # img = Image.open('static/UPLOAD/qrimg/{}.png'.format((request.session['UserName'])))
        # img.show()

        # wget.download('new.png')

        context = {
            'UserName': str(request.session['UserName'])
        }

        return render(request,'QR/download_qr.html',context)
