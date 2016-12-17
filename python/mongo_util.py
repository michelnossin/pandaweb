import pandas as pd
import numpy as np
from pymongo import MongoClient

#mongo my settings
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

def read_panda_from_mongo():
    mng_db = _connect_mongo(mongo_server, mongo_port, "", "", mongo_db)
    db_cm = mng_db[mongo_collection]
    df_read = read_mongo(mongo_db, mongo_collection)
    panda = read_mongo(mongo_db, mongo_collection)
    return panda
