import pymysql

def make_connection():
    cn=pymysql.connect(host="localhost",port=3306,user="root",db="courier",passwd="",autocommit=True)
    cur=cn.cursor()
    return cur

#TOTAL PRICE
def total_price(con):
    cur=make_connection()
    cur.execute("select * from bill where con_no="+con+"")
    n=cur.rowcount
    t=0
    if(n>0):
        data=cur.fetchall()
        for d in data:
            t=t+d[7]
    return t

#TOTAL TAX
def total_tax(con):
    cur=make_connection()
    cur.execute("select * from bill where con_no="+con+"")
    n=cur.rowcount
    t=0
    if(n>0):
        data=cur.fetchall()
        for d in data:
            t=t+d[8]
    return t

# Get Agency Name
def agency_name(email):
    cur=make_connection()
    cur.execute("SELECT * FROM  agency_data where email='"+email+"' " )
    n=cur.rowcount
    name="No"
    if(n>0):
        data=cur.fetchone()
        name=data[0]
    return name

#Booking
def get_booking(email):
    cur=make_connection()
    cur.execute("Select * from booking_data where email='"+email+"'")
    data=cur.fetchall()
    return data

#Show Arrival
def show_arrival(email):
    cur=make_connection()
    cur.execute("Select * from booking_data where em_center='"+email+"'")
    data=cur.fetchall()
    return data