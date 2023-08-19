
from django.urls import path
from myserver.User.controller import signUp,login,get_users_data_by_list_of_user_ids #,add_image,get_image

urlpatterns = [
    path('signup/', signUp, name="signUp"),
    path('login/', login, name="login"),
    path('getusersdata/', get_users_data_by_list_of_user_ids, name="getUsersData"),
    # path('img/', add_image, name="addimg"),
    # path('getimg/<str:imgId>', get_image, name="getimg"),
]

