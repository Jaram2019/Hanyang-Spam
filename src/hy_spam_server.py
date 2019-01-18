# -*- coding: utf-8 -*-

import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_restful import Resource, Api
import pickle
import jsonpickle


app = Flask(__name__) # create the application instance
app.config.from_object(__name__) # load config from this file , flaskr.py
api = Api(app)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=None,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

class HellowWorld(Resource):
    def get(self):
        with open ('../MyMessage', 'rb') as fp:
            msg_list = pickle.load(fp)
            print(msg_list[0])
        return msg_list[0]
    
api.add_resource(HellowWorld, '/')


if __name__ == '__main__':
    app.run(port=1234)