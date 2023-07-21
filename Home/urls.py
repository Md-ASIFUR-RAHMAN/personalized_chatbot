from django.urls import path
from .views import *


urlpatterns=[
    path('', home2, name='home2'),
    path('home', home, name='home'),
    path('about', About, name='About'),
    path('test', test, name='test'),
    path('test_another', test_another, name='test_another'),

    path('Dashboard', Dashboard, name='Dashboard'),
    path('Login', Login, name='Login'),
    path('Logout', Logout, name='Logout'),
    path('send_simple_message', send_simple_message, name='send_simple_message'),
    path('verify/<action_id>', verify, name='verify'),
    path('Recover/<action_id>', Recover, name='Recover'),
    path('Services', Services, name='Services'),
    path('Registration', Registration, name='Registration'),
    path('Profile', Profile, name='Profile'),
    path('Profile_Pic_Edit/<action_id>', Profile_Pic_Edit, name='Profile_Pic_Edit'),
    path('Profile_Info_Edit/<action_id>', Profile_Info_Edit, name='Profile_Info_Edit'),

]


