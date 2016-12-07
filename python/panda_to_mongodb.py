#Run using Python 3
import sys
import pandas as pd
import pymongo
import json
import time
import numpy as np
from datetime import datetime
import random
from pymongo import MongoClient

#my settings
mongo_db = "pandawebdb"
mongo_collection = "pandawebcol"
mongo_server = 'localhost'
mongo_port = 27017
num_rows = 20

#Some mongo util functions:
def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db]

def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)
    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)
    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))
    # Delete the _id
    if no_id:
        del df['_id']
    return df

#Sample Panda DataFrame with different types to test
print ("Creating panda Dataframe")
dates = pd.date_range('20130101',periods=num_rows)
df = pd.DataFrame(np.random.randn(num_rows,1),index=dates,columns=['mydouble'])
df['myint'] = np.random.randint(2000, size=num_rows)
aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher','']
words = np.random.choice(aa_milne_arr, num_rows)  #
df['mystring'] = words
df['mydatetime'] = np.random.choice(pd.to_datetime(['04-01-2012 10:00'], dayfirst=True),num_rows)
df['mytimestamp'] = pd.Timestamp('20131213 11:59:59.999999999')
print ("Sample Panda dataframe created")

#Create db and collection
mng_db = _connect_mongo(mongo_server, mongo_port, "", "", mongo_db)
db_cm = mng_db[mongo_collection]
print ("Connected to mongo db")

#Insert our Dataframe per record.
print ("Going to insert rows from Panda Dataframe into mongodb")
db_cm.remove()
db_cm.insert_many(df.to_dict('records'))
print ("Inserted all Dataframe records into mongo db")

#index for quick lookup
for col in df.columns:
    db_cm.create_index([(col, pymongo.ASCENDING)])
print ("Created index on Mongo db collection")

#test lookup examples to optionally print
#readit = db_cm
#readit.find_one()
#readit.find().count()

#or to load in the complete dataframe:
df_read = read_mongo(mongo_db, mongo_collection)
print ("columns after read:" + str(df_read.columns))
print ("types after reading:" + str(df_read.dtypes))
