from django.urls import path
from .views import *


app_name='myapp1'

urlpatterns = [
    path('',base,name = 'base'),
    path('create/',create, name='create_resume'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('contact/',contact,name='contact'),
]
 