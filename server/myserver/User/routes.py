
from django.urls import path
# ,add_image,get_image
from myserver.User.controller import signUp, login, get_users_data_by_list_of_user_ids,add_user_to_group

urlpatterns = [
    path('signup/', signUp, name="signUp"),
    path('login/', login, name="login"),
    path('getusersdata/', get_users_data_by_list_of_user_ids, name="getUsersData"),
    path('addusertogroup/<str:gid>', add_user_to_group, name="addUserToGroup"),
    # path('img/', add_image, name="addimg"),
    # path('getimg/<str:imgId>', get_image, name="getimg"),
]
