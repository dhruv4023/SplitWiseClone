from myserver.database.mongodb import *

# to add new document


def addNewGroupDataDoc(id: str):
    doc = {
        "_id": id,
        "groupMembers": [],
        "entries":  [],
    }
    try:
        validate_document(document=doc, schema=gropuDataSchema)
        return True if groupData.insert_one(doc) is not None else False
    except:
        return False


# to add new entry to entries array
def addNewEntry(uid: str, comment: str, amt: int, gid: str, spliWith: list):
    doc = {
        "eid": str(getUniqueId()),
        "uid": uid,
        "comment": comment,
        "amt": amt,
        "spliWith": spliWith,
        "date":  str(datetime.now()),
    }
    validate_document(document=doc, schema=entriesSchema)
    query = {"_id": gid}
    update = {
        "$push": {"entries": {"$each": [doc], "$position": 0}},
    }

    try:
        return incrementInTotalCollection(gid, uid, amt, spliWith) and updateOne(query, update) != 0
    except:
        return incrementInTotalCollection(gid, uid, -amt, spliWith)


# to add new entry to entries array
def removeAnEntry(uid: str, amt: int, gid: str, spliWith: list, eid: str):
    query = {"_id": gid}
    update = {
        "$pull": {"entries": {"eid": eid}},
    }
    try:
        return incrementInTotalCollection(gid, uid, -amt, spliWith) and updateOne(query, update) != 0
    except:
        return incrementInTotalCollection(gid, uid, amt, spliWith)


# increment total while adiing new transaction
def incrementInTotalCollection(gid: str, uid: str, amt: int, spliWith: list):
    sub = -round((amt/(len(spliWith)+1)), 2)
    add = amt+sub
    # print(add, sub)
    inc_field = {
        "groupMembers.$[u].total": add,
        "groupMembers.$[x].total": sub
    }
    query = {"_id": gid, "groupMembers.uid": {"$in": [uid]+spliWith}}
    update = {"$inc": inc_field}
    array_filter = [{"u.uid": uid}]
    array_filter.append({"x.uid": {"$in": spliWith}})
    return 0 != updateOne(query=query, update=update, array_filter=array_filter)


# to retrive entries
def getEntries(gid: str, startIndex: int, limit: int):
    query = {"_id": gid}
    return groupData.find_one(query, {"groupMembers": 0, "entries": {"$slice": [int(startIndex), int(limit)]}})


# to retrive groupMembers
def getGroupMembers(gid: str):
    query = {"_id": gid}
    return groupData.find_one(query, {"groupMembers": 1})


# common updateOne function
def updateOne(query, update, array_filter=[]):
    return groupData.update_one(query, update, array_filters=array_filter).modified_count
