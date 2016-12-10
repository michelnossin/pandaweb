#!/data/anaconda3/bin/python
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.utils import redirect
from werkzeug.routing import Map, Rule,NotFound
from jsonrpc import JSONRPCResponseManager, dispatcher

apps_root = "C:\\"
my_server = "localhost"
my_port = 8080

import pandas as pd
import numpy as np


@dispatcher.add_method
def search_text(searchStr="rabbit"):
    print ("Search text " + str(searchStr))

    result = "{message: " + str(searchStr) + " }"
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
    app = DispatcherMiddleware(frontend, { '/data':  application } )
    run_simple(my_server, my_port, app, use_debugger=True, use_reloader=False,threaded=True)
