from django.urls import path
from .views import *

urlpatterns = [

    path('ChatAPI/<str:id>', ChatAPI.as_view(),name="ChatAPI"),

]