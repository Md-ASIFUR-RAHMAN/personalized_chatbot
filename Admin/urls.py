from django.urls import path
from .views import *

urlpatterns = [
    path('', Dashboard, name='Dashboard'),
    path('Login', Login, name='Login'),
    path('Add_Member', Add_Member, name='Add_Member'),
    path('Show_Member', Show_Member, name='Show_Member'),
    path('Edit_Member/<member_id>', Edit_Member, name='Edit_Member'),
    path('Delete_Member/<member_id>', Delete_Member, name='Delete_Member'),
    path('Show_chat_Member', Show_chat_Member, name='Show_chat_Member'),

]