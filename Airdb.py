import psycopg2
from Airport import Airport

connection=psycopg2.connect(host="localhost", dbname="Booking", user="postgres", password="avish283")
cur = connection.cursor()

def insertair(air):
    cur.execute("insert into airport values(%s,%s,%s,%s)",(air.getaircity(),air.getairid(),air.getairname(),air.getairtype()))
    connection.commit()
    return True

def viewair():
    cur.execute("select * from airport")
    return cur

def findair(search):
    cur.execute("select * from airport where air_id=%s",(search,))
    return cur




def close():
    cur.close()
    connection.close()