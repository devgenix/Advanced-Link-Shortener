#   Copyright (c) Code Written and Tested by Ahmed Emad in 28/02/2020, 16:53

from django.urls import path

from backend.views import Shorten

app_name = 'backend'

urlpatterns = [
    path('shorten/', Shorten, name='shorten'),
]