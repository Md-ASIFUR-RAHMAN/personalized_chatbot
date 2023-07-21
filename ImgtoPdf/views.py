from django.shortcuts import render, HttpResponse, redirect
from fpdf import FPDF
import os
from PIL import Image
from django.core.files import File
from django.conf import settings
from io import BytesIO
from django.core.files.storage import FileSystemStorage

# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
# Import render module
from django.shortcuts import render
import os

def remove_images_from_static_folder(idd):

    static_folder_path = 'static/UPLOAD/imgtopdf/{}/'.format(idd)  # Replace with the actual path to your static folder

    for filename in os.listdir(static_folder_path):
        file_path = os.path.join(static_folder_path, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            os.remove(file_path)


def remove_pdf_from_static_folder(idd):

    static_folder_path = 'static/UPLOAD/imgtopdf/{}/'.format(idd)  # Replace with the actual path to your static folder

    for filename in os.listdir(static_folder_path):
        file_path = os.path.join(static_folder_path, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('.pdf')):
            os.remove(file_path)


def image_compress_save(image, img_name,action_id):
    im = Image.open(image)  # or self.files['image'] in your form
    # destroy color pew pew
    im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    compressed_image = File(im_io, name=img_name)
    print(settings.STATIC_URL)
    print(settings.STATIC_ROOT)
    print(settings.STATICFILES_DIRS[0])
    FileSystemStorage(location=os.path.join(settings.STATICFILES_DIRS[0], 'UPLOAD', 'imgtopdf',action_id)).save(img_name,
                                                                                                    compressed_image)
def imgtopdfconv(request):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    if request.method == 'GET':
        return render(request,'ImgToPdf/imgcollect.html')

    if request.method == 'POST':

        # remove_pdf_from_static_folder(str(request.session["UserID"]))

        image = request.FILES.getlist('MultiplePicture')
        n = 0
        ar = []

        for i in image:
            n = n + 1
            title_name = request.session["UserName"].replace(' ', '_')
            image_new_name_multi = title_name + "_" + str(n) + '.jpg'
            ar.append(image_new_name_multi)
            image_compress_save(i, image_new_name_multi, str(request.session["UserID"]))

        pdf = FPDF()
        pdf.set_auto_page_break(0)

        remove_pdf_from_static_folder(str(request.session["UserID"]))

        img_list = [x for x in os.listdir('static/UPLOAD/imgtopdf/{}'.format(str(request.session["UserID"])))]

        for img in img_list:
            pdf.add_page()
            image = 'static/UPLOAD/imgtopdf/{}/'.format(str(request.session["UserID"]))+img
            pdf.image(image,w = 190,h =200)

        pdf.output("static/UPLOAD/imgtopdf/{}/{}.pdf".format(str(request.session["UserID"]),request.session["UserName"]))

        remove_images_from_static_folder(str(request.session["UserID"]))
        return render(request,'ImgtoPdf/file.html',context= {'id':str(request.session["UserID"]),'name':request.session["UserName"]})




# def downloadpdf(request):
#
#     if request.method == 'GET':
#         return render(request, 'ImgToPdf/file.html')
#
#     if request.method == 'POST':
#
#         # Define Django project base directory
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         # Define the full file path
#         filepath = BASE_DIR + 'static/UPLOAD/imgtopdf/{}/'.format(str(request.session["UserID"])) + '{}.pdf'.format(request.session["UserName"])
#         # Open the file for reading content
#         path = open(filepath, 'rb')
#         # Set the mime type
#         mime_type, _ = mimetypes.guess_type(filepath)
#         # Set the return value of the HttpResponse
#         response = HttpResponse(path, content_type=mime_type)
#         # Set the HTTP header for sending to browser
#         response['Content-Disposition'] = "attachment; filename=%s" % '{}.pdf'.format(request.session["UserName"])
#         # Return the response value
#         return render(response,'ImgToPdf/file.html')
    # else:
    #     # Load the template
    #     return render(request, 'ImgToPdf/file.html')