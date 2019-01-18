# -*- coding: utf-8 -*-

import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_restful import Resource, Api
from flask_cors import CORS
from src.get_list import *
import pickle
import jsonpickle


app = Flask(__name__) # create the application instance
CORS(app) # allow CORS
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

class HelloWorld(Resource):
    def get(self):
        with open ('./MyMessage', 'rb') as fp:
            msg_list = pickle.load(fp)
        return msg_list

class LoginWorld(Resource):
    def get(self):
        if(request.args.get('id') and request.args.get('id')):
            get_list(request.args.get('id'),request.args.get('password'))
        else:
            return [{"UPMU_GB": "PU00","ID": 0000000,"SENDER_HP_NO": "0000000000","PUSH_READ_DATE": "2099/12/31 00:00:100","PRIORITY": "일반메세지","SEND_DTTM": "2099/12/31 00:00:100","SEND_SEQ": 000,"UUID": "00000000","MESSAGE_DIV": "P","UPMU_GB_NM": "기타","READ_YN": "Y","MESSAGE": "로그인에 실패하셨습니다!!"}]
        with open ('./MyMessage', 'rb') as fp:
            msg_list = pickle.load(fp)
        return msg_list
    
api.add_resource(HelloWorld, '/')
api.add_resource(LoginWorld, '/login/')

if __name__ == '__main__':
    app.run(port=1234)
