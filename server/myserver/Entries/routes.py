
from django.urls import path
from myserver.Entries.controller import *


urlpatterns = [
    path('add/<str:uid>/<str:gid>', add_entries, name="addentries"),
    path('delete/<str:uid>/<str:gid>/<str:eid>', delete_entries, name="deleteentries"),
    path('get/<str:gid>/<int:startIndex>/<int:limit>', get_entries, name="getentries"),
    path('getgroupmemberdata/<str:gid>', get_getGroup_members_data, name="getgroupmemberdata"),
]


