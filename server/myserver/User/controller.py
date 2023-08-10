import json
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from myserver.database.user import addNewuser, getUserDetails
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
            password = body.get('password')
            hashed_password = make_password(password)
            res = addNewuser(_id, name, email, hashed_password) # calling function to add new user data
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
            userData = getUserDetails(_id, email) # retrive data from database as per given user email or _id
            hashed_password = userData["password"]
            userData["password"] = None
            password_valid = check_password(password, hashed_password) # inbuilt fun to verify the entered password with has password
            if password_valid:
                return HttpResponse(json.dumps({"msg": "Log in success", "userData": userData}), content_type='application/json')
            return HttpResponse(json.dumps({"msg": "Invalid Credentials"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        # if any error occurs than 
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
