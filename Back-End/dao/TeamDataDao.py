import os,sys
from config import DevConfig
import datetime
from datetime import date
import time
#import sqlalchemy as db
from base import engine, Session, Base
from objects.TotalsInfo import TotalsInfo
from objects.PKInfo import PKInfo
from objects.PointSpreadsInfo import PointSpreadsInfo

def init():
    Base.metadata.create_all(engine)

def queryDataByType(type):
    #connection = engine.connect()
    #query = db.select([init(GAME_DATA)])
    #ResultProxy = connection.execute(query)
    #ResultSet = ResultProxy.fetchall()
    #print(ResultSet)
    return ''

def queryTeamData(team):
    init()
    session = Session()
    stmt = session.query(PKInfo.TEAM.label('MatchUp'),PKInfo.RESULT.label('PK'),\
           PointSpreadsInfo.RESULT.label('PointSpreads'),\
           TotalsInfo.RESULT.label('Totals'),\
           TotalsInfo.SCORE.label('Score'),\
           TotalsInfo.GAME_TIME.label('Date')).join(PointSpreadsInfo, PKInfo.id == PointSpreadsInfo.id)\
           .join(TotalsInfo, PointSpreadsInfo.id == TotalsInfo.id)\
           .filter(PKInfo.TEAM.like('%,' + team))\
           .order_by(PKInfo.GAME_TIME.desc())\
           .subquery()
    data = session.query(stmt).all()[0:10]    
    return data