from sqlalchemy import Column, String, Integer, Date
from base import Base

class PKInfo(Base):
    __tablename__ = 'PK_DATA'

    id=Column(Integer, primary_key=True)
    TEAM=Column(String)
    TRENDS=Column(String)
    ODDS=Column(String)
    RESULT=Column(String)
    GAME_TIME=Column(Date)
    CREATE_TIME=Column(Date)
    CATEGORY=Column(String)

    def __init__(self, id, team, trends, odds, result, gameTime, createTime, category):
        self.id = id
        self.TEAM = team
        self.TRENDS = trends
        self.ODDS = odds
        self.RESULT = result
        self.GAME_TIME = gameTime
        self.CREATE_TIME = createTime
        self.CATEGORY = category