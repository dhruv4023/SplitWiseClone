
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from myserver.home import *

urlpatterns = [
    path('user/', include('myserver.User.routes')),
    path('entry/', include('myserver.Entries.routes')),
    path('group/', include('myserver.Group.routes')),
]
