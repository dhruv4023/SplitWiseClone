
from django.urls import path
from myserver.Group.controller import *


urlpatterns = [
    path('add/<str:uid>', add_group, name="addgroup"),
    path('delete/<str:gid>/<str:uid>', delete_group, name="deletegroup"),
    path('get/<str:u_id>/<str:gid>', get_group_data, name="getgroup"),
]


