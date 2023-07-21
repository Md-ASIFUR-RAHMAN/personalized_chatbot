from django.urls import path
from .views import *


urlpatterns=[
    path('convert', imgtopdfconv, name='imgtopdfconv'),
    # path('download', downloadpdf, name='downloadpdf'),

]