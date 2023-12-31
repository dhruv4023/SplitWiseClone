import json
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from myserver.database.group import *


@csrf_exempt
def add_group(request, uid):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            groupName = body.get("groupName")
            x = addNewGroup(groupName=groupName, userName=uid)
            if x:
                return HttpResponse(json.dumps({"msg": "added"}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({"msg": "failed to add"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def delete_group(request, gid, uid):
    try:
        if request.method == 'DELETE':
            body = json.loads(request.body)
            splitWith = body.get("splitWith")
            amt = body.get("amt")
            if removeGroup(id=gid, uid=uid):
                return HttpResponse(json.dumps({"msg": "deleted "+gid}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({"msg": "failed to delete "+gid}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def get_group(request, gid):
    try:
        if request.method == 'GET':
            return HttpResponse(json.dumps({"group": getGroupData(gid=gid)}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
