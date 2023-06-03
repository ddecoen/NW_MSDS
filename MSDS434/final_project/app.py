import os
import requests
import bq

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class QueryData(Resource):
    def get(self):
        return bq.run_()

api.add_resource(QueryData, '/')

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
