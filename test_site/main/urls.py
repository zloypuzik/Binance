from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('', index,  name='index'),
    path('test/', test, name='test'),

]

