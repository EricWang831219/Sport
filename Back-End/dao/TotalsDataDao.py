import os,sys
from config import DevConfig
import datetime
from datetime import date
import time
#import sqlalchemy as db
from base import engine, Session, Base
from objects.TotalsInfo import TotalsInfo

def init():
    Base.metadata.create_all(engine)

def insert(itemList):
    init()
    # create a new session
    session = Session()
    session.add_all(itemList)
    session.commit()
    session.close()

def queryOverTotalsCount():
    init()
    session = Session()
    totals = session.query(TotalsInfo).count()
    overCounts = session.query(TotalsInfo).filter_by(RESULT = 1).count()
    return overCounts/totals   

def queryAll():
    init()
    session = Session()
    return session.query(TotalsInfo).all()

def queryOverTotals():
    init()
    session = Session()
    data = session.query(TotalsInfo).filter_by(RESULT = 1)
    return data