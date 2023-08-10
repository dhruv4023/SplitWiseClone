
from django.urls import path
from myserver.Entries.controller import *


urlpatterns = [
    path('add/<str:u_id>', add_entries, name="addentries"),
    path('delete/<str:u_id>', delete_entries, name="deleteentries"),
    path('get/<str:u_id>/<str:startIndex>', get_entries, name="getentries"),
]


