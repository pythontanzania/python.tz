# pythontz/urls.py

from pythontz.views import Home

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
]
