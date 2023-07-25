from django.urls import path
from .views import *


urlpatterns=[

    path('pay', getapi_withpay, name='getapi_withpay'),
    path('payadvance', getapi_advance, name='getapi_advance'),
    path('paypro', getapi_pro, name='getapi_pro'),
    path('trial', getapi_trial, name='getapi_trial'),
    path('paymentt', paymentt, name='paymentt'),
    path('ssl', ssl, name='ssl'),

]