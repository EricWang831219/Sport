import os,sys

from flask import request
from flask_cors import CORS
from config import DevConfig
from bs4 import BeautifulSoup
from flask_jsonpify import jsonpify
import datetime
from datetime import date

import time
import numpy as np
import pandas as pd
import requests as rq
from service import OrganizeDataService as ocs

#取得div的Id
def getId(s):
    format = '0123456789'
    for c in s:
        if c not in format:
            s = s.replace(c,'')
    return s    
#設定request 並取得response
def initRequestAndGetResponse(id, timeS, category):
    timeStr = str(time).replace('-','')
    if(category == 'NBA'):
        Referer = 'https://classic.sportsbookreview.com/betting-odds/nba-basketball/?date='
    else:
        Referer = 'https://classic.sportsbookreview.com/betting-odds/mlb-baseball/?date='
    url = 'https://classic.sportsbookreview.com/ajax/?a=[SBR.Odds.Modules]OddsEvent_GetConsensus'
    payload = {
        'UserId': '0',
        'Sport': 'basketball',
        'League': 'NBA',
        'EventId': id,
        'View': 'CO',
        'SportsbookId': '0',
        'DefaultBookId': '0',
        'ConsensusBookId': '19',
        'PeriodTypeId': '',
        'StartDate': timeS,
        'MatchupLink': 'https://classic.sportsbookreview.com/betting-odds/nba-basketball/golden-state-warriors-vs-boston-celtics-' + id + '/',
        'Key': 'ec7fbd5935fc25d86592d3e48eea2d68',
        'theme': 'Blue',
    }
    headers = {
        'Host': 'classic.sportsbookreview.com',
        'Origin': 'https://classic.sportsbookreview.com',
        'Referer': Referer + timeStr
    }
    r = rq.post(url, data=payload, headers=headers)
    r.headers['Access-Control-Allow-Origin'] = '*'
    r.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    r.headers['Access-Control-Allow-Headers'] = 'x-requested-with'

    return r

def getIdList(time):
    url = 'http://classic.sportsbookreview.com/betting-odds/nba-basketball/?date=' + str(time).replace('-','')
    response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
    soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
    
    resultList = []
    for div in soup.find_all("div", class_= "event-holder"):
        teamList = []
        homeScore = []
        awayScore = []
        for teamValue in div.find_all("span", class_="team-name"):
            teamList.append(teamValue.text)
        for awayScoreV in div.find_all("span", class_="first period"):
            awayScore.append(awayScoreV.text)
        awayScore.append(div.find_all("span", class_="first total ")[0].text)
        for homeScoreV in div.find_all("span", class_=" period"):
            homeScore.append(homeScoreV.text)
        homeScore.append(div.find_all("span", class_="total ")[0].text)
        resultList.append(dict(id=getId(div['id']), homeTeam=teamList[1], awayTeam=teamList[0], homeScore=homeScore, awayScore=awayScore))
    return resultList

def getIdListForMLB(time):
    url = 'https://classic.sportsbookreview.com/betting-odds/mlb-baseball/?date=' + str(time).replace('-','')
    response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
    soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
    
    resultList = []
    for div in soup.find_all("div", class_= "event-holder"):
        teamList = []
        homeScore = []
        awayScore = []
        for teamValue in div.find_all("span", class_="team-name"):
            teamList.append(teamValue.text)  
        awayScore.append(div.find_all("span", class_="first total")[0].text)
        homeScore.append(div.find_all("span", class_="total")[1].text)
        resultList.append(dict(id=getId(div['id']), homeTeam=teamList[1], awayTeam=teamList[0], homeScore=homeScore, awayScore=awayScore))
    return resultList

def getContent(idList, time,category):      
    allData = [] #存所有資料

    for obj in idList: 
        response = initRequestAndGetResponse(obj["id"], time, category)
        soup = BeautifulSoup(response.text, 'lxml')

        datas = []
        datas.append(obj)   
        for data in soup.find_all("div", class_="info-box"):
            datas.append(data)    
        allData.append(datas)
    return allData
    
  
