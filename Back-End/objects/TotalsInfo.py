from sqlalchemy import Column, String, Integer, Date
from base import Base

class TotalsInfo(Base):
    __tablename__ = 'TOTALS_DATA'

    id=Column(Integer, primary_key=True)
    TEAM=Column(String)
    TRENDS=Column(String)
    ODDS=Column(String)
    HANDICAP=Column(String)
    RESULT=Column(String)
    SCORE=Column(String)
    GAME_TIME=Column(Date)
    CREATE_TIME=Column(Date)
    CATEGORY=Column(String)

    def __init__(self, id, team, trends, odds, handicap, result, score, gameTime, createTime, category):
        self.id = id
        self.TEAM = team
        self.TRENDS = trends
        self.ODDS = odds
        self.HANDICAP = handicap
        self.RESULT = result
        self.SCORE = score
        self.GAME_TIME = gameTime
        self.CREATE_TIME = createTime
        self.CATEGORY = category