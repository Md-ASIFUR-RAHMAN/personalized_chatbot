from django.urls import path
from .views import *


urlpatterns=[

    path('pay', getapi, name='getapi'),

]