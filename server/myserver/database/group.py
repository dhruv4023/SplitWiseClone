from myserver.database.mongodb import *
from myserver.database.groupData import addNewGroupDataDoc

# to add new document
def addNewGroup(userName: str, groupName: str):
    id=generateId()
    doc = {
        "_id": id,
        "groupName": groupName,
        "groupCreatedBy":  userName,
        "groupCreatedOn": str(datetime.now()),
    }
    try:
        validate_document(document=doc, schema=groupSchema)
        if groups.insert_one(doc).inserted_id is not None and addNewGroupDataDoc(id):
            return True 
        else:
            groups.delete_one({"_id":id}) 
            return False
    except:
        return False

def removeGroup(id:str,uid:str):
    query={"_id":id}
    if groups.find_one(query)["groupCreatedBy"]==uid:
        return groupData.delete_one(query) and groups.delete_one(query)
    return False

def getGroupData(gid:str):
    query={"_id":gid}
    return groups.find_one(query)