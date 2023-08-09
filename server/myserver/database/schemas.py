# schema for user collection
usersSchema = {
    "_id": str,
    "name": str,
    "email": str,
    "password": str,
}

# schema for entriesMethods and archived collection
groupSchema = {
    "_id": str,
    "groupName": str,
    "groupCreatedBy": str,
    "groupCreatedOn": str,
}

gropuDataSchema = {
    "_id": str,
    "groupMembers": list,
    "entries": list
}

groupMemberSchema = {
    "uid": str,
    "total": int,
}

entriesSchema = {
    "eid": str,
    "uid": str,
    "comment": str,
    "amt": int,
    "spliWith": list,
    "date": str,
}


def validate_document(document, schema):
    for field, field_type in schema.items():
        if field not in document:
            raise ValueError(f"Missing field: {field}")
        if not isinstance(document[field], field_type):
            raise ValueError(
                f"Invalid field type for {field}. Expected: {field_type.__name__}, Actual: {type(document[field]).__name__}")
