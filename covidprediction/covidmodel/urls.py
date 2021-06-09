from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('license/',license,name='license'),
    path('form/',form,name='form'),
    path('results/',results,name='results')
]