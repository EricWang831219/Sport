#encoding:utf-8
import os,sys
sys.path.append("C:\ServerHome\Anaconda3\Lib\site-packages")
from flask import Flask,render_template, request,make_response,jsonify
from flask_cors import CORS
from config import DevConfig
from bs4 import BeautifulSoup
from flask_jsonpify import jsonpify
from functools import wraps
import numpy as np
import pandas as pd
import requests as rq
from facade import SportAnalyzeFacade
from service import StoreDataService
import json

app = Flask(__name__,
static_folder = "../../Front-End/Vue/dist/static",
template_folder = "../../Front-End/Vue/dist"
)
app.config.from_object(DevConfig)
CORS(app, resources=r'/*')

@app.route('/index')
def init():
    #result = storeDataService.queryDataByType("")
    #result = GameDataDao.recordGameDataToDB("", "")
    return render_template('index.html')

@app.route('/getData', methods=['GET', 'POST'])
def getData():
    category = request.args.get('category')
    result = SportAnalyzeFacade.collectData(category)
    
    return ''#render_template('index.html')

@app.route('/getPercent', methods=['GET', 'POST'])
def getPercent():
    response = SportAnalyzeFacade.getProportion()
    return jsonify(response)

@app.route('/getTeamData', methods=['GET', 'POST'])
def getTeamData():
    team = request.args.get('team')
    dataList = SportAnalyzeFacade.getTeamData(team)
    return json.dumps(dataList)#jsonify(response)

@app.route('/getPrediction', methods=['GET', 'POST'])
def getPrediction():
    data = request.args.get('data')
    category = request.args.get('category')
    response = SportAnalyzeFacade.getPrediction(data,category)
    return jsonify(response)

@app.route('/training', methods=['GET', 'POST'])
def training():
    response = SportAnalyzeFacade.training()
    return jsonify(response)

if __name__ == '__main__':
    app.run()
