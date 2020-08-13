class Customer():

    def __init__(self):
        self.cust_name=''
        self.cust_id=0
        self.mob=''
        self.bookings=[]



    def setcname(self,name):
        self.cust_name=name

    def setcid(self,id):
        self.cust_id=id

    def setcmob(self,mob):
        self.mob=mob

    def setbookings(self,fly):
        self.bookings.append(fly)

    def getcname(self):
        return self.cust_name

    def getcid(self):
        return self.cust_id

    def getcmob(self):
        return self.mob

    def getbookings(self):
        return self.bookings