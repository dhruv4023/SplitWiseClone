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

def removeGroup(id:str):
    return groupData.delete_one({"_id":id}) and groups.delete_one({"_id":id})