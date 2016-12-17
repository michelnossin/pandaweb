import json
from flask import Flask, jsonify, abort, request, make_response, url_for, Response
from flask.ext.httpauth import HTTPBasicAuth
from pymongo import MongoClient
import pandas as pd
import numpy as np
import mongo_util as mu
from flask_cors import CORS, cross_origin

#You would normally use this to return json from each apihandyman: return jsonify( { 'key': value } )
#However our Griddle component expects an array of json objects so we use json.dump

#Lets creates our API backend
app = Flask(__name__, static_url_path = "")
CORS(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'pandaweb':
        return 'pandaweb'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( "Unauthorized access" ), 403)
    #return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/pandaweb/all', methods = ['GET', 'OPTIONS'])
def find_all():
    js = eval(mu.read_panda_from_mongo().to_json(orient="records"))
    return Response(json.dumps(js),  mimetype='application/json') #json.dumps(js_array)

@app.route('/pandaweb/range/<int:from_id>/<int:to_id>', methods = ['GET','OPTIONS'])
def find_by_range(from_id,to_id):
    js = eval(mu.read_panda_from_mongo().iloc[from_id:to_id].to_json(orient="records"))  #or use the _id in mongo
    return Response(json.dumps(js),  mimetype='application/json')

@app.route('/pandaweb/delete/<int:db_id>', methods = ['DELETE'])
@auth.login_required
def delete(db_id):
    return jsonify( "Deleted element OK" )

if __name__ == '__main__':
    app.run(debug = True,port=3000, host='localhost')
