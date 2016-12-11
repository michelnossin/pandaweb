#!/data/anaconda3/bin/python
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.utils import redirect
from werkzeug.routing import Map, Rule,NotFound
from jsonrpc import JSONRPCResponseManager, dispatcher
import pandas as pd
import numpy as np
import pymongo

apps_root = "C:\\"  #Todo later change to location to host our frontend files
my_server = "localhost"
#port to start backend jsonrpc server on , notice frontend will also use this port when using this python example
my_port = 3001
my_path = "/data"  #path used to use the backend

#my settings for Mongodb
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

#Lets define our JSONRPC backend functions
@dispatcher.add_method
def search_text(searchStr="rabbit"):
    print ("Search text " + str(searchStr))
    df_read = read_mongo(mongo_db, mongo_collection)

    result = "{message: 'Real data from mongodb!', datatable: " + df_read.to_json() + " }"
    return result

class Application(object):

    def __init__(self):
        dummy = 0

    def dispatch_request(self, request):
        return Response('This is not the full url B:)')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
        response.headers['Cache-Control'] = 'public, max-age=0'
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

def createApplication():
    app = Application()
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/': apps_root
        })
    return app

@Request.application
def application(request):
    dispatcher["search_text"] = search_text

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)

    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    frontend = createApplication()
    app = DispatcherMiddleware(frontend, { my_path :  application } )
    run_simple(my_server, my_port, app, use_debugger=True, use_reloader=False,threaded=True)
