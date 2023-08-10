
from django.urls import path
from myserver.Entries.controller import *


urlpatterns = [
    path('add/<str:uid>/<str:gid>', add_entries, name="addentries"),
    path('delete/<str:uid>/<str:gid>/<str:eid>', delete_entries, name="deleteentries"),
    path('get/<str:gid>/<str:startIndex>/<str:limit>', get_entries, name="getentries"),
]


