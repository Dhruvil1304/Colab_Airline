from Airport import Airport

class Flight:

    def __init__(self):
        self.id=0
        self.source=''
        self.destination=''
        self.date=1-1-20
        self.landing=0
        self.takeoff=0
        self.classs=''
        self.via=''
        self.airline=''

    def setvia(self,via):
        self.via=via

    def setairline(self,airline):
        self.airline=airline

    def setsource(self,source):
        self.source=source

    def setdesti(self,desti):
        self.destination=desti

    def setid(self,id):
        self.id=id

    def setdate(self,date):
        self.date=date

    def setclasss(self,classs):
        self.classs=classs

    def settakeoff(self,takeoff):
        self.takeoff=takeoff

    def setlanding(self,land):
        self.landing=land


    def getid(self):
        return self.id

    def getdate(self):
        return self.date

    def getclasss(self):
        return self.classs

    def gettakeoff(self):
        return self.takeoff

    def getlanding(self):
        return self.landing

    def getsource(self):
        return self.source

    def getdesti(self):
        return self.destination

    def getvia(self):
        return self.via

    def getairline(self):
        return self.airline


