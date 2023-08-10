from myserver.database.mongodb import *


# signup
def addNewuser(_id: str, name: str, email: str, password: str):
    doc = {
        "_id": _id,
        "name": name,
        "email": email,
        "password": password,
    }
  
    if users.count_documents({"_id":_id},limit=1)==1:
        return False
    validate_document(document=doc, schema=usersSchema)
    users.insert_one(doc)
    return True


# log in
def getUserDetails(_id: str, email: str):
    u = None
    if _id is not None:
        u = users.find_one({"_id": _id})
    elif email is not None:
        u = users.find_one({"email": email})
    else:
        return None
    return u
