# dbからdataを所得する
import pymongo
from pymongo import MongoClient
import pandas as pd

client = pymongo.MongoClient('localhost', 27017)

db = client.naist2021
dbcol = db.codesaves
df = pd.DataFrame(list(dbcol.find()))
#print(df)
print(df[df.userID == 's44'])