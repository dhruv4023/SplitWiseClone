from myserver.database.schemas import *
from myserver.database.uniqueId import *
from datetime import datetime
from pymongo import MongoClient
from django.conf import settings
import ssl


DB_URL = "mongodb://localhost:27017"
# DB_URL = settings.DB_URL


# adding not adding the security by Secure Socket Layer
client = MongoClient(DB_URL, ssl_cert_reqs=ssl.CERT_NONE)

# DB_URL = "mongodb://localhost:27017"

print("database connected successfully")

db = client["SplitWise"]

# all collections
users = db["users"]
groups = db["groups"]
groupData = db["gropuData"]
