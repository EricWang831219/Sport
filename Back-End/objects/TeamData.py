import json

class TeamData:
    def __init__(self, matchUP, PK, pointSpreads, totals, score, gametime):
        self.matchUP = matchUP
        self.PK = PK
        self.pointSpreads = pointSpreads
        self.totals = totals
        self.score = score
        self.gameTime = gametime