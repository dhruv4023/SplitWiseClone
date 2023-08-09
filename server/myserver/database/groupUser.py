from myserver.database.groupData import updateOne
from myserver.database.mongodb import *


def addUserToGrp(uid: str, gid: str):
    doc = {
        "uid": uid,
        "total": 0,
    }
    validate_document(document=doc, schema=groupMemberSchema)
    update = {
        "$push": {"groupMembers": doc},
    }
    return updateOne({"_id": gid}, update) !=0

def removeUserFromGrp(uid: str, gid: str):
    update = {
        "$pull": {
            "groupMembers": {
                "uid": uid
            }
        },
    }
    return updateOne({"_id": gid}, update) !=0
