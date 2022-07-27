from flask import Flask,request,render_template,session,url_for,redirect
from mylib import *

app=Flask(__name__)
app.secret_key="super secret key"

#welcome
@app.route("/",methods=['GET','POST'])
def welcome():
    if (request.method == "POST"):
        con = request.form["T1"]
        p = total_price(con)
        w = total_tax(con)
        bill = p + w
        cur = make_connection()
        sql = "select * from booking_data where con_no=" + con + ""
        sql1 = "select * from tracking where con_no=" + con + ""
        cur.execute(sql)
        data = cur.fetchall()
        cur.execute(sql1)
        n = cur.rowcount
        if (n > 0):
            data1 = cur.fetchall()
            return render_template("record.html", kota=data, kota1=data1, bill=bill)
        else:
            return render_template("welcome.html")
    else:
        return render_template("welcome.html")

#login
@app.route("/login",methods=['GET','POST'])
def login():
    if(request.method=="POST"):
        email=request.form["T1"]
        pas=request.form["T2"]

        cur=make_connection()
        sql="select * from login_data where email='"+email+"' AND password='"+pas+"'"

        cur.execute(sql)
        n=cur.rowcount
        if(n>0):
            data=cur.fetchone()
            ut=data[2]
            session["email"]=email
            session["usertype"]=ut
            if(ut=="admin"):
                return redirect(url_for("adminhome"))
            elif(ut=="agency"):
                return redirect(url_for("agency_home"))
            elif(ut=="client"):
                return redirect(url_for("clienthome"))
            else:
                return render_template("login.html",msg="Invalid usertype,Contact to admin")
        else:
            return render_template("login.html",msg="Either userid or password is incorrect")
    else:
        return render_template("login.html")

#Adminhome
@app.route("/adminhome")
def adminhome():
    if("usertype" in session):
        ut=session["usertype"]
        if(ut=="admin"):
            return render_template("adminhome.html")
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Admin Registration
@app.route("/admin_reg",methods=['GET','POST'])
def admin_reg():
    if("usertype" in session):
        ut=session["usertype"]
        if(ut=="admin"):
            if(request.method=="POST"):
                nm=request.form["T1"]
                ad=request.form["T2"]
                co=request.form["T3"]
                email=request.form["T4"]
                pas=request.form["T5"]
                usertype="admin"

                cur=make_connection()
                sql="insert into admin_data values('"+nm+"','"+ad+"','"+co+"','"+email+"')"
                sql1="insert into login_data values('"+email+"','"+pas+"','"+usertype+"')"

                try:
                    cur.execute(sql)
                    n=cur.rowcount

                    cur.execute(sql1)
                    m=cur.rowcount

                    if(n==1 and m==1):
                        msg="Data saved"
                    else:
                        msg="Data not saved"
                except pymysql.err.IntegrityError:
                    msg="Data already registered"
                return render_template("admin_reg.html",result=msg)
            else:
                return render_template("admin_reg.html")
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Admin Change Password
@app.route("/admin_password",methods=['GET','POST'])
def admin_password():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="admin"):
            if(request.method=="POST"):
                op=request.form["T1"]
                np=request.form["T2"]

                cur=make_connection()
                sql="update login_data set password='"+np+"' where email='"+email+"' AND password='"+op+"'"
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    return render_template("admin_password.html",result="Password changed successfully")
                else:
                    return render_template("admin_password.html",result="Password not changed")
            else:
                return render_template("admin_password.html")
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Admin profile
@app.route("/admin_profile")
def admin_profile():
    if("usertype" in session):
        ut=session["usertype"]
        if(ut=="admin"):
            cur=make_connection()
            email = session["email"]
            sql="select * from admin_data where email='"+email+"'"
            cur.execute(sql)
            n=cur.rowcount
            if(n>0):
                data=cur.fetchone()
                return render_template("admin_profile.html",kota=data)
            else:
                return render_template("admin_profile.html",msg="No data found")
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Admin profile1
@app.route("/admin_profile1",methods=['GET','POST'])
def admin_profile1():
    if("usertype" in session):
        ut=session["usertype"]
        if(ut=="admin"):
            if(request.method=="POST"):
                cur=make_connection()
                email=session["email"]
                sql="select * from admin_data where email='"+email+"'"
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    data=cur.fetchone()
                    return render_template("admin_profile1.html",kota=data,msg="Data saved")
                else:
                    return render_template("admin_profile1.html",msg="Data not saved")
            else:
                return redirect(url_for("admin_profile"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Admin profile2
@app.route("/admin_profile2",methods=['GET','POST'])
def admin_profile2():
    if("usertype" in session):
        ut=session["usertype"]
        if(ut=="admin"):
            if(request.method=="POST"):
                nm=request.form["T1"]
                ad=request.form["T2"]
                co=request.form["T3"]
                email=session["email"]

                cur=make_connection()
                sql="update admin_data set name='"+nm+"',address='"+ad+"',contact='"+co+"' where email='"+email+"'"
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    return render_template("admin_profile2.html",msg="Data saved")
                else:
                    return render_template("admin_profile2.html",msg="Data not saved")
            else:
                return redirect(url_for("admin_profile"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Agency's Branch
@app.route("/state",methods=['GET','POST'])
def state():
    if ("usertype" in session):
        ut = session["usertype"]
        if (ut == "admin"):
            if (request.method == "POST"):
                state = request.form["T1"]
                c1= request.form["T2"]
                c2 = request.form["T3"]
                c3= request.form["T4"]
                c4 = request.form["T5"]

                cur = make_connection()
                sql = "insert into state_data values('" + state + "','" + c1 + "','" + c2 + "','"+c3+"','"+c4+"')"

                try:
                    cur.execute(sql)
                    n = cur.rowcount

                    if (n == 1):
                        msg = "Data saved"
                    else:
                        msg = "Data not saved"
                except pymysql.err.IntegrityError:
                    msg = "Data already registered"
                return render_template("state.html", msg=msg)
            else:
                return render_template("state.html")
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Show Agency's Branch
@app.route("/show_branch")
def show_branch():
    if("usertype" in session):
        ut=session["usertype"]
        if(ut=="admin"):
            cur=make_connection()
            sql="select * from state_data"
            cur.execute(sql)
            n=cur.rowcount
            if(n>0):
                data=cur.fetchall()
                return render_template("show_state.html",kota=data)
            else:
                return render_template("show_state.html",msg="No data found")
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Show booking details
@app.route("/admin_show_booking_list")
def admin_show_booking_list():
    if("usertype" in session):
        ut=session["usertype"]
        if(ut=="admin"):
            cur=make_connection()
            sql="select * from booking_data"
            cur.execute(sql)
            n=cur.rowcount
            if(n>0):
                data=cur.fetchall()
                return render_template("admin_show_booking_list.html",kota=data)
            else:
                return render_template("admin_show_booking_list.html",msg="Data not found")
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Agency Reg
@app.route("/agency_reg",methods=['GET','POST'])
def agency_reg():
            if(request.method=="POST"):
                nm=request.form["T1"]
                ad=request.form["T2"]
                city=request.form["T3"]
                state=request.form["T4"]
                co=request.form["T5"]
                email=request.form["T6"]
                pas=request.form["T7"]
                usertype="agency"

                cur=make_connection()
                sql="insert into agency_data values('"+nm+"','"+ad+"','"+city+"','"+state+"','"+co+"','"+email+"')"
                sql1="insert into login_data values('"+email+"','"+pas+"','"+usertype+"')"

                try:
                    cur.execute(sql)
                    n=cur.rowcount

                    cur.execute(sql1)
                    m=cur.rowcount

                    if(n==1 and m==1):
                        msg="Data saved"
                    else:
                        msg="Data not saved"
                except pymysql.err.IntegrityError:
                    msg="Data already registered"
                return render_template("agency_reg.html",result=msg)
            else:
                return render_template("agency_reg.html")

#Admin Search
@app.route("/search",methods=['GET','POST'])
def search():
    if("usertype" in session):
        ut=session["usertype"]
        if(ut=="admin"):
            if(request.method=="POST"):
                con=request.form["T1"]
                cur=make_connection()
                sql="select * from booking_data where con_no="+con+""
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    data=cur.fetchall()
                    return render_template("admin_show_booking.html",kota=data)
                else:
                    return render_template("admin_show_booking.html",msg="*Enter the valid consignment number")
            else:
                return redirect(url_for("show_booking"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Agencyhome
@app.route("/agency_home")
def agency_home():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            name=agency_name(email)
            return render_template("agency_home.html",name=name)
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Booking
@app.route("/booking_reg",methods=['GET','POST'])
def booking_reg():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            name = agency_name(email)
            if(request.method=="POST"):
                nm=agency_name(email)
                dt=request.form["T1"]
                st=request.form["T2"]
                fc=request.form["T3"]
                s1=request.form["T4"]
                tc=request.form["T5"]
                sn=request.form["T6"]
                sa=request.form["T7"]
                sc=request.form["T8"]
                rn=request.form["T9"]
                ra=request.form["T10"]
                rc=request.form["T11"]
                w=request.form["T12"]
                email_of_center = email
                em=request.form["T14"]


                cur=make_connection()
                sql="insert into booking_data values(0,'"+nm+"','"+dt+"','"+st+"','"+fc+"','"+s1+"','"+tc+"','"+sn+"','"+sa+"','"+sc+"','"+rn+"','"+ra+"','"+rc+"',"+w+",'"+email_of_center+"','"+em+"')"

                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    return render_template("booking.html",msg="Successfully Booked",name=name)
                else:
                    return render_template("booking.html",msg="Error",name=name)
            else:
                return render_template("booking.html",name=name)
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Show booking details
@app.route("/show_booking")
def show_booking():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            name = agency_name(email)
            cur=make_connection()
            sql="select * from booking_data where email='"+email+"'"
            cur.execute(sql)
            n=cur.rowcount
            if(n>0):
                data=cur.fetchall()
                return render_template("show_booking.html",kota=data,name=name)
            else:
                return render_template("show_booking.html",msg="Data not found")
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#BILL
@app.route("/bill",methods=['GET','POST'])
def bill():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            name = agency_name(email)
            if(request.method=="POST"):
                c=request.form["T1"]
                a=request.form["T2"]
                d=request.form["T3"]
                nm=request.form["T4"]
                ad=request.form["T5"]
                con=request.form["T6"]
                w=request.form["T7"]
                p=request.form["T8"]
                tc=request.form["T9"]

                cur=make_connection()
                sql="insert into bill values("+c+",'"+a+"','"+d+"','"+nm+"','"+ad+"','"+con+"',"+w+","+p+","+tc+")"
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    return render_template("bill.html",result="Data saved")
                else:
                    return render_template("bill.html",result="Data not saved")
            else:
                return render_template("bill.html",name=name)
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Show BILL
@app.route("/show_bill",methods=['GET','POST'])
def show_bill():
    if ("usertype" in session):
        ut = session["usertype"]
        email=session["email"]
        if (ut == "agency"):

            if(request.method=="POST"):
                name = agency_name(email)
                con=request.form["H1"]
                p=total_price(con)
                t=total_tax(con)
                bill=p+t
                cur = make_connection()
                sql = "select * from bill where con_no="+con+""
                cur.execute(sql)
                n = cur.rowcount
                if (n > 0):
                    data = cur.fetchall()
                    return render_template("show_bill.html", kota=data,bill=bill,name=name)
                else:
                    return render_template("show_bill.html", msg="No data found")
            else:
                return redirect(url_for("show_booking"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Edit bill
@app.route("/edit_bill",methods=['GET','POST'])
def edit_bill():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            if(request.method=="POST"):
                name = agency_name(email)
                con=request.form["H1"]
                cur=make_connection()
                sql="select * from bill where con_no="+con+""
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    data=cur.fetchone()
                    return render_template("edit_bill.html",kota=data,name=name)
                else:
                    return render_template("edit_bill.html",msg="Data Not Found")
            else:
                return  redirect(url_for("show_bill"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Edit bill 1
@app.route("/edit_bill1",methods=['GET','POST'])
def edit_bill1():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            if(request.method=="POST"):
                name = agency_name(email)
                c=request.form["T1"]
                an = request.form["T2"]
                dt = request.form["T3"]
                nm = request.form["T4"]
                ad = request.form["T5"]
                co = request.form["T6"]
                w = request.form["T7"]
                p = request.form["T8"]
                tc = request.form["T9"]

                cur=make_connection()
                sql="update bill set agency='"+an+"', date='"+dt+"',sender_name='"+nm+"',sender_address='"+ad+"',contact='"+co+"',weight="+w+",price="+p+",tax="+tc+" where con_no="+c+""
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    return render_template("edit_bill1.html",msg="Data saved",name=name)
                else:
                    return render_template("edit_bill1.html",msg="Data not saved")
            else:
                return redirect(url_for("show_bill"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Edit booking details
@app.route("/edit_booking",methods=['GET','POST'])
def edit_booking():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            if(request.method=="POST"):
                name = agency_name(email)
                c=request.form["H1"]
                cur=make_connection()
                sql="select * from booking_data where con_no="+c+""
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    data=cur.fetchone()
                    return render_template("edit_booking.html",kota=data,name=name)
                else:
                    return render_template("edit_booking.html",msg="No data saved")
            else:
                return redirect(url_for("show_booking"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Edit booking1 details
@app.route("/edit_booking1",methods=['GET','POST'])
def edit_booking1():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            if(request.method=="POST"):
                name = agency_name(email)
                c=request.form["T1"]
                dt = request.form["T2"]
                st = request.form["T3"]
                fc = request.form["T4"]
                s1 = request.form["T5"]
                tc = request.form["T6"]
                sn = request.form["T7"]
                sa = request.form["T8"]
                sc = request.form["T9"]
                rn = request.form["T10"]
                ra = request.form["T11"]
                rc = request.form["T12"]
                w = request.form["T13"]

                cur=make_connection()
                sql="update booking_data set date='"+dt+"',state='"+st+"',from_city='"+fc+"',state_name_1='"+s1+"',to_city='"+tc+"',sender_name='"+sn+"',sender_address='"+sa+"',contact='"+sc+"',receiver_name='"+rn+"',receiver_address='"+ra+"',receiver_contact='"+rc+"',weight="+w+" where con_no="+c+""
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    return render_template("edit_booking1.html",msg="Data saved",name=name)
                else:
                    return render_template("edit_booking1.html",msg="Data not saved")
            else:
                return redirect(url_for("show_booking"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Delete booking
@app.route("/delete_booking",methods=['GET','POST'])
def delete_booking():
    if("usertype" in session):
        ut=session["usertype"]
        if(ut=="agency"):
            if(request.method=="POST"):
                c=request.form["H1"]
                cur = make_connection()
                sql = "delete from booking_data where con_no=" + c + ""
                sql1 = "delete from bill where con_no=" + c + ""
                sql2 = "delete from tracking where con_no=" + c + ""
                cur.execute(sql)
                n = cur.rowcount

                cur.execute(sql1)
                m=cur.rowcount

                cur.execute(sql2)
                p=cur.rowcount

                if (n == 1 and m==1 and p==1):
                    data = cur.fetchone()
                    return render_template("delete_booking.html", kota=data, msg=" Data Deleted")
                else:
                    return render_template("delete_booking.html", msg=" Data Deleted")
            else:
                return redirect(url_for("show_booking"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Insertion  Tracking
@app.route("/tracking",methods=['GET','POST'])
def tracking():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            name = agency_name(email)
            if(request.method=="POST"):
                con=request.form["T1"]
                d=request.form["T2"]
                t=request.form["T3"]
                off=request.form["T4"]
                e=request.form["T5"]
                cur=make_connection()
                sql="insert into tracking values("+con+",'"+d+"','"+t+"','"+off+"','"+e+"')"
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    return render_template("tracking.html",msg="Data saved")
                else:
                    return render_template("tracking.html",msg="Data not saved")
            else:
                return render_template("tracking.html",name=name)
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Show tracking details
@app.route("/show_tracking",methods=['GET','POST'])
def show_tracking():
    email=session["email"]
    if(request.method=="POST"):
        name = agency_name(email)
        con=request.form["H1"]
        cur=make_connection()
        sql="select * from tracking where con_no="+con+""
        cur.execute(sql)
        n=cur.rowcount
        if(n>0):
            data=cur.fetchall()
            return render_template("show_tracking.html",kota=data,name=name)
        else:
            return render_template("show_tracking.html")
    else:
        return redirect(url_for("show_booking"))

#Edit Tracking
@app.route("/edit_tracking",methods=['GET','POST'])
def edit_tracking():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            if(request.method=="POST"):
                name = agency_name(email)
                con=request.form["H1"]
                cur=make_connection()
                sql="select * from tracking where con_no="+con+""
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    data=cur.fetchone()
                    return render_template("edit_tracking.html",kota=data,name=name)
                else:
                    return render_template("edit_tracking.html",msg="Data Not Found")
            else:
                return  redirect(url_for("show_tracking"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Edit Tracking 1
@app.route("/edit_tracking1",methods=['GET','POST'])
def edit_tracking1():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            if(request.method=="POST"):
                name = agency_name(email)
                c=request.form["T1"]
                dt = request.form["T2"]
                t = request.form["T3"]
                off = request.form["T4"]
                e = request.form["T5"]

                cur=make_connection()
                sql="update tracking set date='"+dt+"',time='"+t+"',office='"+off+"',event='"+e+"' where con_no="+c+""
                cur.execute(sql)
                n=cur.rowcount
                if(n==1):
                    return render_template("edit_tracking1.html",msg="Data saved",name=name)
                else:
                    return render_template("edit_tracking1.html",msg="Data not saved")
            else:
                return redirect(url_for("show_tracking"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Search
@app.route("/search_con",methods=['GET','POST'])
def search_con():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):

            if(request.method=="POST"):
                name = agency_name(email)
                show = show_arrival(email)
                con=request.form["T1"]
                cur=make_connection()
                sql="select * from booking_data where con_no="+con+" AND email='"+email+"'"

                try:
                    cur.execute(sql)
                    n=cur.rowcount
                    if(n==1):
                        data=cur.fetchall()
                        return render_template("show_search.html",kota=data,name=name,show=show)
                    else:
                        return render_template("show_search.html",msg="*Enter the valid consignment number",name=name)
                except pymysql.err.ProgrammingError:
                        return render_template("show_search.html",msg="*Enter the valid consignment number",name=name)
            else:
                return redirect(url_for("show_booking"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Incoming Search
@app.route("/in_con",methods=['GET','POST'])
def in_con():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            if(request.method=="POST"):
                name = agency_name(email)
                con=request.form["T1"]
                cur=make_connection()
                sql="select * from booking_data where con_no="+con+" AND em_sender='"+email+"'"

                try:
                    cur.execute(sql)
                    n=cur.rowcount
                    if(n==1):
                        data=cur.fetchall()
                        return render_template("show_search_in.html",kota=data,name=name)
                    else:
                        return render_template("show_search_in.html",msg="*Enter the valid consignment number",name=name)
                except pymysql.err.ProgrammingError:
                        return render_template("show_search_in.html",msg="*Error",name=name)
            else:
                return redirect(url_for("arrival"))
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

#Online Booking
@app.route("/online_booking",methods=['GET','POST'])
def online_booking():
    if(request.method=="POST"):
        type="Online Booking"
        dt = request.form["T2"]
        st = request.form["T3"]
        fc = request.form["T4"]
        s1 = request.form["T5"]
        tc = request.form["T6"]
        sn = request.form["T7"]
        sa = request.form["T8"]
        sc = request.form["T9"]
        rn = request.form["T10"]
        ra = request.form["T11"]
        rc = request.form["T12"]
        w = request.form["T13"]

        cur=make_connection()
        sql="insert into booking_data values(0,'"+type+"','"+dt+"','"+st+"','"+fc+"','"+s1+"','"+tc+"','"+sn+"','"+sa+"','"+sc+"','"+rn+"','"+ra+"','"+rc+"',"+w+")"
        cur.execute(sql)
        n=cur.rowcount
        if(n==1):
            return render_template("online_booking.html",msg="Successfully booked")
        else:
            return render_template("online_booking.html",msg="Please enter carefully")
    else:
        return render_template("online_booking.html")

#Incoming Booking
@app.route("/arrival",methods=['GET','POST'])
def arrival():
    if("usertype" in session):
        ut=session["usertype"]
        email=session["email"]
        if(ut=="agency"):
            name = agency_name(email)
            show=show_arrival(email)
            return render_template("incoming_booking.html",kota=show,name=name)
        else:
            return render_template("incoming_booking.html",msg="Data not found",name=name)
    else:
        return redirect(url_for("auth_error"))

#logout
@app.route("/logout",methods=['GET','POST'])
def logout():
    if("usertype" in session):
        session.pop("usertype",None)
        session.pop("email",None)
        return redirect(url_for("welcome"))
    else:
        return redirect(url_for("welcome"))

#Authorization Error
@app.route("/auth_error")
def auth_error():
    return render_template("auth_error.html")

#main function
if __name__=="__main__":
    app.run(debug=True)