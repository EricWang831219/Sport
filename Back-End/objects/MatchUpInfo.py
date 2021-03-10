class MatchUpInfo:
    def __init__(self):
        self._matchUp = None #[who VS who]
        self._homeTeamScore = [] #['21','20','20','20','81']
        self._awayTeamScore = [] #['21','20','20','20','81']
        self._totalsDic = {} #['221,-108,53','220,-110,55',....]
        self._moneyLinesDic = {} #['+700,55','+655,56',....]
        self._pointSpreadsDic = {} #['+4.5,-103,45','+4.5,-105,43',...]
        self._gameResult = []
        
    @property
    def matchUp(self):
        return self._matchUp
    
    @matchUp.setter
    def matchUp(self, value):
        self._matchUp = value

    @property
    def homeTeamScore(self):
        return self._homeTeamScore
    
    @homeTeamScore.setter
    def homeTeamScore(self, value):
        self._homeTeamScore = value

    @property
    def awayTeamScore(self):
        return self._awayTeamScore

    @awayTeamScore.setter
    def awayTeamScore(self, value):
        self._awayTeamScore = value

    @property
    def totalsDic(self):
        return self._totalsDic

    @totalsDic.setter
    def totalsDic(self, value):
        self._totalsDic = value

    @property
    def moneyLinesDic(self):
        return self._moneyLinesDic

    @moneyLinesDic.setter
    def moneyLinesDic(self, value):
        self._moneyLinesDic = value

    @property
    def pointSpreadsDic(self):
        return self._pointSpreadsDic

    @pointSpreadsDic.setter
    def pointSpreadsDic(self, value):
        self._pointSpreadsDic = value   

    @property
    def gameResult(self):
        return self._gameResult
    
    @gameResult.setter
    def gameResult(self, value):
        self._gameResult = value

    