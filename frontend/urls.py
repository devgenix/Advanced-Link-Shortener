#   Copyright (c) Code Written and Tested by Ahmed Emad in 28/02/2020, 16:53

from django.urls import path

from frontend.views import home
from backend.views import Redirect

app_name = 'frontend'

urlpatterns = [
    path('', home),
    path('<str:url>', Redirect, name='redirect'),
    
]