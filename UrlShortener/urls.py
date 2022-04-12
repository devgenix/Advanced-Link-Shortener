#   Copyright (c) Code Written and Tested by Ahmed Emad in 28/02/2020, 16:53

from django.contrib import admin
from django.urls import path, include
from backend.views import Shorten

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shorten/', Shorten, name='api-backend'),
    path('', include('frontend.urls'), name="api-frontend")
]
