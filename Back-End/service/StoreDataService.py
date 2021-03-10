import os,sys
from config import DevConfig
import datetime
from datetime import date
import time

from objects.PointSpreadsInfo import PointSpreadsInfo
from objects.PKInfo import PKInfo
from objects.TotalsInfo import TotalsInfo
from dao import PointSpreadsDataDao,PKDataDao,TotalsDataDao


def recordGameDataToDB(idList, cleanData, time):
    pointSpreadsInfo = None
    pKInfo = None
    totalsInfo = None
    psList = []
    pkList = []
    tList = []
    for item in idList:
        obj = cleanData[item['id']]
        pointSpreadsInfo = PointSpreadsInfo(item['id'], obj.matchUp, ','.join(obj.pointSpreadsDic['trandsD']), ','.join(obj.pointSpreadsDic['oddsD']), ','.join(obj.pointSpreadsDic['handicapD']), obj.gameResult[0],datetime.datetime.strptime(time, '%Y-%m-%d'),datetime.datetime.now(), 'NBA')
        pKInfo = PKInfo(item['id'], obj.matchUp, ','.join(obj.moneyLinesDic['trandsD']), ','.join(obj.moneyLinesDic['oddsD']), obj.gameResult[1],datetime.datetime.strptime(time, '%Y-%m-%d'),datetime.datetime.now(), 'NBA')
        totalsInfo = TotalsInfo(item['id'], obj.matchUp, ','.join(obj.totalsDic['trandsD']), ','.join(obj.totalsDic['oddsD']), ','.join(obj.totalsDic['handicapD']), obj.gameResult[2],obj.homeTeamScore[-1],datetime.datetime.strptime(time, '%Y-%m-%d'),datetime.datetime.now(), 'NBA')
        psList.append(pointSpreadsInfo)
        pkList.append(pKInfo)
        tList.append(totalsInfo)
    PointSpreadsDataDao.insert(psList)
    PKDataDao.insert(pkList)
    TotalsDataDao.insert(tList)

def recordGameDataToDBForMLB(idList, cleanData, time):
    pointSpreadsInfo = None
    psList = []
    for item in idList:
        obj = cleanData[item['id']]
        pointSpreadsInfo = PointSpreadsInfo(item['id'], obj.matchUp, ','.join(obj.pointSpreadsDic['trandsD']), ','.join(obj.pointSpreadsDic['oddsD']), ','.join(obj.pointSpreadsDic['handicapD']), obj.gameResult[0],datetime.datetime.strptime(time, '%Y-%m-%d'),datetime.datetime.now(), 'MLB')
        psList.append(pointSpreadsInfo)
    PointSpreadsDataDao.insert(psList)