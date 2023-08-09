
from django.urls import path
from myserver.EntryMethod.controller import *


urlpatterns = [
    path('add/<str:u_id>', add_entries, name="addentries"),
    path('delete/<str:u_id>', delete_entries, name="deleteentries"),
    path('edit/<str:u_id>/<str:entryId>', edit_entries, name="editentries"),
    path('changelable/<str:u_id>', changelable_entries, name="changelableentries"),
    path('get/<str:u_id>/<str:startIndex>', get_entries, name="getentries"),
]


