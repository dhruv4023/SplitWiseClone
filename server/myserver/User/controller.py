import json
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from myserver.database.user import addNewuser, getUserDetails, getUsersData #, addImage, getImage
from django.contrib.auth.hashers import make_password, check_password


# http://127.0.0.1:8000/expense/user/signup/
# {
#   "_id": "abc",
#   "name": "ab_nm",
#   "email": "ab_e",
#   "password": "pass"
# }


@csrf_exempt
def signUp(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            _id = body.get("_id")
            name = body.get('name')
            email = body.get('email')
            imgPath = body.get('imgPath')
            password = body.get('password')
            hashed_password = make_password(password)
            # calling function to add new user data
            res = addNewuser(_id, name, email, hashed_password, imgPath)
            if res:
                # addNewUser fun will return True if no other user exist with given _id
                return HttpResponse(json.dumps({"msg": "Sign up successfully!"}), content_type='application/json')
            else:
                # addNewUser fun will return False if other user exist with given _id
                return HttpResponse(json.dumps({"msg": "User with "+_id+" Already Exist!"}), content_type='application/json')

    except:
        # if any error occurs than
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


# http://127.0.0.1:8000/expense/user/login/
# {
#   "_id": "abdc",
#   "password": "pass"
# }
@csrf_exempt
def login(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            _id = body.get("_id")
            email = body.get('email')
            password = body.get('password')
            # retrive data from database as per given user email or _id
            userData = getUserDetails(_id, email)
            hashed_password = userData["password"]
            userData["password"] = None
            # inbuilt fun to verify the entered password with has password
            password_valid = check_password(password, hashed_password)
            if password_valid:
                return HttpResponse(json.dumps({"msg": "Log in success", "userData": userData}), content_type='application/json')
            return HttpResponse(json.dumps({"msg": "Invalid Credentials"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        # if any error occurs than
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def get_users_data_by_list_of_user_ids(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            # print(body.get('user_ids'))
            return HttpResponse(json.dumps({"group": getUsersData(user_ids=body.get('user_ids'))}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


# @csrf_exempt
# def add_image(req):
#     body = json.loads(req.body)
#     return HttpResponse(json.dumps({"msg": addImage(path=body.get("imgPath"))}), content_type='application/json')

# @csrf_exempt
# def get_image(req,imgId):
#     # return getImage(imgId=imgId)
#     return HttpResponse(json.dumps({"msg":getImage(imgId=imgId)}), content_type='application/json')
