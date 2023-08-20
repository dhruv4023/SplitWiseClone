import json
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from myserver.database.groupData import *


@csrf_exempt
def add_entries(request, uid, gid):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            comment = body.get("comment")
            splitWith = body.get("splitWith")
            amt = body.get("amt")
            x = addNewEntry(uid=uid, amt=amt, comment=comment,
                            gid=gid, spliWith=splitWith)
            if x:
                return HttpResponse(json.dumps({"msg": "added"}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({"msg": "failed to add"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def delete_entries(request, uid, gid, eid):
    try:
        if request.method == 'DELETE':
            body = json.loads(request.body)
            splitWith = body.get("splitWith")
            amt = body.get("amt")
            if removeAnEntry(uid=uid, amt=amt, eid=eid, gid=gid, spliWith=splitWith):
                return HttpResponse(json.dumps({"msg": "deleted "+eid}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({"msg": "failed to delete "+eid}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def get_entries(request, gid, startIndex, limit=10):
    try:
        if request.method == 'GET':
            return HttpResponse(json.dumps({"data": getEntries(gid=gid, startIndex=startIndex, limit=limit)}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

@csrf_exempt
def get_getGroup_members_data(request, gid):
    try:
        if request.method == 'GET':
            return HttpResponse(json.dumps({"data": getGroupMembers(gid=gid)}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
