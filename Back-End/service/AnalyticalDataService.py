import sys

import numpy as np
import pandas as pd
from dao import PKDataDao
from dao import PointSpreadsDataDao
from dao import TotalsDataDao

dataSetByPointSpreads = []
dataSetByTotals = []

def isFloat(num):
    try:
        return int(num)
    except ValueError:
        return float(num)

def getDataArray(data):
    arr = []
    for i in range(5): #取最新的5個盤口   
        if data[i] == "" :
            data[i] = '0'
        arr.append(isFloat(data[i].replace('+','')))            
    return arr

def getDataList(data):
    dataList = []
    d = data.split('|')
    for s in d:
        numList = []
        numSet = s.split(',')
        for num in numSet:
            numList.append(float(num))
        dataList.append(numList)
    return dataList   

def predictionResult(data, category):
    dataArray = getDataList(data)
    curTrends = dataArray[0]
    curOdds = dataArray[1]
    curHandicap = dataArray[2]
    print(category)

    #Step1: 取出DB資料
    global dataSetByPointSpreads
    if len(dataSetByPointSpreads) == 0 :
        dataSetByPointSpreads = PointSpreadsDataDao.queryAll(category)

    #Step2: 計算出person相關係數
    totals = 0
    winHandicap = 0
    for data in dataSetByPointSpreads: #totals > 8 才列入計算
        trendsStr = data.TRENDS.split(',')
        oddsStr = data.ODDS.split(',')
        handicapStr = data.HANDICAP.split(',')
        if len(trendsStr) >=7 :
            dfTrends = pd.DataFrame({'curTrends':curTrends,'pastTrends':getDataArray(trendsStr)})
            dfOdds = pd.DataFrame({'curOdds':curOdds,'pastOdds':getDataArray(oddsStr)})
            dfHandicap = pd.DataFrame({'curHandicap':curHandicap,'pastHandicap':getDataArray(handicapStr)})
            #and (dfOdds.corr().iat[0,1]) >=0.5
            if(category == 'NBA'):
                if (dfTrends.corr().iat[0,1]) >= 0.85 and (dfHandicap.corr().iat[0,1]) >= 0.85:
                    totals = totals + 1
                    if data.RESULT == '1':
                        winHandicap = winHandicap + 1
            else:
                if (dfTrends.corr().iat[0,1]) >= 0.85 and (dfOdds.corr().iat[0,1]) >= 0.85:
                    totals = totals + 1
                    if data.RESULT == '1':
                        winHandicap = winHandicap + 1
    result = dict(winRate=winHandicap/totals if totals!=0 else 0, totals=totals)    #過盤機率            
    return result

