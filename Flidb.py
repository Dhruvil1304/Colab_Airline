import psycopg2
from Flight import Flight

connection=psycopg2.connect(host="localhost", dbname="Booking", user="postgres", password="avish283")
cur = connection.cursor()

def insertfli(f1):
    cur.execute("insert into flight values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(f1.getid(),f1.getsource(),f1.getdesti(),f1.getdate(),f1.gettakeoff(),f1.getclasss(),f1.getairline(),f1.getvia(),f1.getlanding()))
    connection.commit()
    return True

def viewfli():
    cur.execute("select * from flight")
    return cur

def findfli(id):
    cur.execute("select * from flight where fli_id=%s",(id,))
    return cur

def available(source):
    cur.execute("select * from flight where fli_source=%s",(source,))
    return cur

def avail(source,desti):
    cur.execute("select * from flight where fli_source=%s and fli_desti=%s", (source,desti))
    return cur



def close():
    cur.close()
    connection.close()