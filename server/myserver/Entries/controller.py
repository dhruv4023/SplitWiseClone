import json
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from myserver.database.group import addNewEntry, deleteEntry, editentriesComment, changelableentries, getentries


@csrf_exempt
def add_entries(request, u_id):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            comment = body.get("comment")
            amt = body.get("amt")
            labelId = body.get("labelId")
            x = addNewEntry(
                userId=u_id, comment=comment, amt=amt, labelId=labelId)
            # print(x)
            if x:
                return HttpResponse(json.dumps({"msg": "added"}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({"msg": "failed to add"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def delete_entries(request, u_id):
    try:
        if request.method == 'DELETE':
            body = json.loads(request.body)
            trasactionData = body.get("entrydata")
            if deleteEntry(entryMethodId=u_id, trasactionData=trasactionData):
                return HttpResponse(json.dumps({"msg": "deleted "+trasactionData["entryId"]}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({"msg": "failed to delete "+trasactionData["entryId"]}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def edit_entries(request, u_id, entryId):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            if editentriesComment(entryMethodId=u_id, entryId=entryId, comment=body.get("comment")):
                return HttpResponse(json.dumps({"msg": "comment edited"}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({"msg": "comment edit failed"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def changelable_entries(request, u_id):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            trasactionData = body.get("entrydata")
            newLabelId = body.get("newLabelId")
            if changelableentries(entryMethodId=u_id, newLabelId=newLabelId, trasactionData=trasactionData):
                return HttpResponse(json.dumps({"labels": "label changed"}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({"labels": "label change failed"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def get_entries(request, u_id, startIndex):
    try:
        if request.method == 'GET':
            return HttpResponse(json.dumps({"entries": getentries(entryMethodId=u_id, startIndex=startIndex)}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
