import pymongo
from pymongo import MongoClient
import pandas as pd

client = pymongo.MongoClient('localhost', 27017)

db = client.naist2021
dbcol = db.chatinfos
df1 = pd.DataFrame(list(dbcol.find()))
df = df1.sort_values(['room', 'date']) # dfの並べ替え
df['date'] = df['date'].astype(str) #date列のみを文字列変換
df = df[df['date'].str.contains('2021-04-21')]
df.to_excel("April21data.xlsx", sheet_name = "sheet1", index = True, header = True)

# print(
    
#     df[df['date'].str.contains('2021-04-21')]

# )