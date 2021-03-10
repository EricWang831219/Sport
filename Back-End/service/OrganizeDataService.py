import sys

from flask import Flask,render_template, request
import datetime
from datetime import date

from objects.MatchUpInfo import MatchUpInfo

def cleanData(data):

    return""

#將多餘的字元去掉
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text   


def getDataAfterProcessing(data): 
    cleanData = []
    for index, d in enumerate(data.find_all("td")):
        if index % 3 == 2 and index != 2:
            cleanData.append(processingData(d))
    return cleanData

def processingData(d):
    resultData = d.text.replace(' ','').rstrip().replace('%','') #EX:+5\xa0-105\xa049
    resultData = resultData.replace("½",".5") #EX: +12.5\xa0-105\xa042
    return resultData.replace("\xa0",",") #EX:+12.5,-103,49

def splitData(list, type):
    trends = []
    odds = []
    handicap = []
    for item in list:
        itemValue = item.split(",")
        if type == 'PK':
            odds.append(itemValue[0])
            trends.append(itemValue[1])
        else:
            handicap.append(itemValue[0])
            odds.append(itemValue[1])
            trends.append(itemValue[2])   
    return dict(trandsD=trends, oddsD=odds, handicapD=handicap)

def getGameResult(dataObject):
    gameResult = [] #讓分盤/PK盤/大小分盤
    homeTeamTotalScore = dataObject.homeTeamScore[-1]
    awayTeamTotalScore = dataObject.awayTeamScore[-1]
    gameTotalScore = int(homeTeamTotalScore) + int(awayTeamTotalScore)
    
    pointSpreads = dataObject.pointSpreadsDic['handicapD'][0]
    totals = dataObject.totalsDic['handicapD'][0]
    #讓分盤結果
    if '+' in pointSpreads:
        num = float(pointSpreads.replace('+',''))
        gameResult.append((float(homeTeamTotalScore) + num) > float(awayTeamTotalScore))
    else:
        num = float(pointSpreads.replace('-',''))
        gameResult.append((float(homeTeamTotalScore) - num) > float(awayTeamTotalScore))
    #PK盤結果
    gameResult.append(int(homeTeamTotalScore) > int(awayTeamTotalScore))
    #大小分盤結果
    gameResult.append(float(gameTotalScore) > float(totals))

    return gameResult

def getGameResultForMLB(dataObject):
    gameResult = [] #讓分盤/PK盤/大小分盤
    homeTeamTotalScore = dataObject.homeTeamScore[0]
    awayTeamTotalScore = dataObject.awayTeamScore[0]
    
    pointSpreads = dataObject.pointSpreadsDic['handicapD'][0]
    #讓分盤結果
    if '+' in pointSpreads:
        num = float(pointSpreads.replace('+',''))
        gameResult.append((float(homeTeamTotalScore) + num) > float(awayTeamTotalScore))
    else:
        num = float(pointSpreads.replace('-',''))
        gameResult.append((float(homeTeamTotalScore) - num) > float(awayTeamTotalScore))

    return gameResult

def organisingMaterials(datas): #整理資料
    dataDict = {}
    #Step1: 將每場賽事資訊 分成:pointSpreads/moneyLines/totals 資訊
    for data in datas:
        dataObject = MatchUpInfo()
        #1-1: 取得賽事ID,主客隊資訊
        dataObject.matchUp = data[0]['awayTeam'] + ',' + data[0]['homeTeam']
        dataObject.homeTeamScore = data[0]['homeScore']
        dataObject.awayTeamScore = data[0]['awayScore']

        #1-1: 取得賽事讓分盤資訊
        dataObject.pointSpreadsDic = splitData(getDataAfterProcessing(data[1]), 'pointSpreads')
        
        #1-2: 取得賽事PK盤資訊
        dataObject.moneyLinesDic = splitData(getDataAfterProcessing(data[2]), 'PK')

        #1-3: 取得賽事大小分盤資訊
        dataObject.totalsDic = splitData(getDataAfterProcessing(data[3]), 'totals')

        #1-4: 取得賽事結果
        dataObject.gameResult = getGameResult(dataObject)

        dataDict[data[0]['id']] = dataObject
    return dataDict

def organisingMaterialsForMLB(datas):
    dataDict = {}
    for data in datas:
        dataObject = MatchUpInfo()
        #1-1: 取得賽事ID,主客隊資訊
        dataObject.matchUp = data[0]['awayTeam'][0:data[0]['awayTeam'].find("\xa0")] + ',' + data[0]['homeTeam'][0:data[0]['homeTeam'].find("\xa0")]
        print(dataObject.matchUp)
        #1-1: 取得賽事讓分盤資訊
        dataObject.pointSpreadsDic = splitData(getDataAfterProcessing(data[1]), 'pointSpreads')
        #1-2: 取得賽事結果
        dataObject.homeTeamScore = data[0]['homeScore']
        dataObject.awayTeamScore = data[0]['awayScore']
        dataObject.gameResult = getGameResultForMLB(dataObject)

        dataDict[data[0]['id']] = dataObject
    return dataDict    