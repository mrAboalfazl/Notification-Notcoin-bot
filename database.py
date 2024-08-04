import time
import requests
import schedule
import pymongo
from datetime import datetime

# Client creation
dbclient = pymongo.MongoClient(
    "mongodb://root:example@82.115.17.181:2712/"
)

# Create db or use if exist
data_db = dbclient["UserInformation"]

# Create collection or use if exist
information_user_collection = data_db["UserInformationDocument"]

# information_user_collection.f

#Function insert 
def creat_Document(dataUser, countKeys):
    dataUser["time"] = datetime.now()
    dataUser["timestamp"] = time.time()
    dataUser["userInformation"]["count_keys"] = countKeys
    information_user_collection.insert_one(dataUser)