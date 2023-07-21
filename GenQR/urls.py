from django.urls import path
from .views import *


urlpatterns=[
    path('qr', Generate_QR, name='Generate_QR'),

]