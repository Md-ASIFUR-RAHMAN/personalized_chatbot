from django.urls import path
from .views import *


urlpatterns=[

    path('faq', faq, name='faq'),
    path('test', Test, name='Test'),
    path('chat/<action_id>', chat,name='chat'),
    path('update/<pk>', update,name='update'),
    path('delete/<pk>', delete,name='delete'),

]