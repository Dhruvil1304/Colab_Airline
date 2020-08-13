class Airport():
    def __init__(self):
        self.id=0
        self.name=''
        self.city=''
        self.type='dom'

    def setairid(self,id):
        self.id = id

    def setairname(self,name):
        self.name=name

    def setaircity(self,city):
        self.city=city

    def setairtype(self,type):
        self.type=type


    def getairid(self):
        return self.id

    def getairname(self):
        return self.name

    def getaircity(self):
        return self.city

    def getairtype(self):
        return self.type



