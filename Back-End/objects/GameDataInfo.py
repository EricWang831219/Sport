from sqlalchemy import Column, String, Integer, Date
from base import Base

class GameDataInfo(Base):
    __tablename__ = 'GAME_DATA'

    id=Column(Integer, primary_key=True)
    TEAM=Column(String)
    HOMETEAM_SCORE=Column(String)
    AWAYTEAM_SCORE=Column(String)
    POINTSPREADS=Column(String)
    MONEYLINES=Column(String)
    TOTALS=Column(String)
    CREATE_TIME=Column(Date)

    def __init__(self, id, team, homeTeamScore, awayTeamScore, pointSpreads, moneyLines, totals, date):
        self.id = id
        self.TEAM = team
        self.HOMETEAM_SCORE = homeTeamScore
        self.AWAYTEAM_SCORE = awayTeamScore
        self.POINTSPREADS = pointSpreads
        self.MONEYLINES = moneyLines
        self.TOTALS = totals
        self.CREATE_TIME = date