import os,sys

from config import DevConfig
from bs4 import BeautifulSoup
from flask_jsonpify import jsonpify
import datetime
from datetime import date

import time
from service import DataCollectionService as dcs
from service import OrganizeDataService as ocs
from service import StoreDataService as sds
from service import AnalyticalDataService
from dao import TotalsDataDao
from dao import TeamDataDao
from objects.TeamData import TeamData
import json
import csv

#收集資料並存入DB
def collectData(category):
    startdate = datetime.datetime(2019, 3,28)
    enddate = datetime.datetime(2019,3,28) #最後更新日期

    if(category == 'NBA'):
        collectDataForNBA(startdate, enddate)
    else:
        collectDataForMLB(startdate, enddate)    
    return 'SUCCESS' 

def collectDataForNBA(startdate, enddate):
    totaldays = (enddate - startdate).days + 1
    for daynumber in range(totaldays):
        datestring = (startdate + datetime.timedelta(days = daynumber)).date()
        #step 1: 至網頁將資料爬下來
        idList = dcs.getIdList(datestring.strftime("%Y-%m-%d")) #1-1: 取得每場賽事的ID,以供後面記錄及取得賽事資訊
        datas = dcs.getContent(idList, datestring.strftime("%Y-%m-%d"), 'NBA') #1-2: 透過ID取得賽事資訊  

        #step 2: 資料整理
        cleanData = ocs.organisingMaterials(datas)

        #step 3: 存入DB
        sds.recordGameDataToDB(idList, cleanData, datestring.strftime("%Y-%m-%d"))
    return 'SUCCESS'

def collectDataForMLB(startdate, enddate):
    totaldays = (enddate - startdate).days + 1
    for daynumber in range(totaldays):
        datestring = (startdate + datetime.timedelta(days = daynumber)).date()
        #step 1: 至網頁將資料爬下來
        idList = dcs.getIdListForMLB(datestring.strftime("%Y-%m-%d")) #1-1: 取得每場賽事的ID,以供後面記錄及取得賽事資訊
        datas = dcs.getContent(idList, datestring.strftime("%Y-%m-%d"), 'MLB') #1-2: 透過ID取得賽事資訊  
        #step 2: 資料整理
        cleanData = ocs.organisingMaterialsForMLB(datas)

        #step 3: 存入DB
        sds.recordGameDataToDBForMLB(idList, cleanData, datestring.strftime("%Y-%m-%d"))
    return 'SUCCESS'

#取得目前賽季大小分比例狀況
def getProportion(): 
    result = TotalsDataDao.queryOverTotalsCount()
    response = {
        'OverPercent': str(((float)("%.4f" % result) * 100) )
    }
    return response

def getTeamData(team):
    resultList = []
    dataList = TeamDataDao.queryTeamData(team)
    for data in dataList:
        resultList.append(TeamData(data.MatchUp, data.PK, data.PointSpreads, data.Totals, data.Score, data.Date.strftime("%Y-%m-%d")).__dict__)
    return resultList 

def getPrediction(data, category):
    result = AnalyticalDataService.predictionResult(data, category)
    winRate = ((float)("%.4f" % result['winRate']) * 100) 
    response = {
        'winRate': str(winRate),
        'totals': str(result['totals'])
    }
    return response

def training():
    dataStr = ''
    resultList = []
    gameResultList = [0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]
    totals = 0
    correct = 0
    with open('data.csv', newline='') as csvfile:
    
     # 以冒號分隔欄位，讀取檔案內容
        rows = csv.reader(csvfile, delimiter=':')
        for index, row in enumerate(rows):
            dataStr = row[0] + '|' + row[1] + '|' + row[2]
            result = AnalyticalDataService.predictionResult(dataStr)
            winRate = ((float)("%.4f" % result['winRate']) * 100) 
            if result['totals'] >= 5 :
                totals = totals + 1
                if (winRate > 50 and gameResultList[index] == 1) or (winRate < 50 and gameResultList[index] == 0):
                    correct = correct + 1
            #resultList.append(dict(winRate=winRate, totals = result['totals'], index=index+1))
    response = {
        'Correct rate': ((float)("%.4f" % (correct/totals)) * 100) 
    }
    print(totals)
    print(correct)
    return response
