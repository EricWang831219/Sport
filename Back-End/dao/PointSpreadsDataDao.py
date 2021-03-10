import os,sys
from config import DevConfig
import datetime
from datetime import date
import time
#import sqlalchemy as db
from base import engine, Session, Base
from objects.PointSpreadsInfo import PointSpreadsInfo

def init():
    Base.metadata.create_all(engine)

def insert(itemList):
    init()
    # create a new session
    session = Session()
    session.add_all(itemList)
    session.commit()
    session.close()

def queryAll(category):
    init()
    session = Session()
    return session.query(PointSpreadsInfo).filter_by(CATEGORY = category)  
