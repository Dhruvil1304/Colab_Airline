import psycopg2
from Customer import Customer

connection=psycopg2.connect(host="localhost", dbname="Booking", user="postgres", password="avish283")
cur = connection.cursor()

def insertcust(c1):
    cur.execute("insert into customers values(%s,%s,%s,%s)",(c1.getcname(),c1.getcid(),c1.getcmob(),c1.getbookings()))
    connection.commit()
    return True

def viewcust():
    cur.execute("select * from customers")
    return cur

def findcust(id):
    cur.execute("select * from customers where cust_id=%s",(id,))
    return cur

def close():
    cur.close()
    connection.close()