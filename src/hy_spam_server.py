import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_restful import Resource, Api


app = Flask(__name__) # create the application instance
app.config.from_object(__name__) # load config from this file , flaskr.py
api = Api(app)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# database connection
def connect_db():
    """Connects to the sqlite3"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

class HellowWorld(Resource):
    def get(self):
        return {'hello': 'waasssss'}
    
api.add_resource(HellowWorld, '/')


if __name__ == '__main__':
    app.run(port=1234)