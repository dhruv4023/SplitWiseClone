
from django.urls import path
from myserver.User.controller import signUp,login,get_users_data_by_list_of_user_ids

urlpatterns = [
    path('signup/', signUp, name="signUp"),
    path('login/', login, name="login"),
    path('getusersdata/', get_users_data_by_list_of_user_ids, name="getUsersData"),
]

