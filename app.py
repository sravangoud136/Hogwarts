from SqlConnection import getSqlConnection
from flask import Flask,jsonify,request,render_template,redirect,session,url_for
import Students_dao
import json
app = Flask(__name__)
app.secret_key = "sravan"
cnx=getSqlConnection()

@app.route('/Home')
def Home():
    return render_template('index.html')
@app.route('/login')
def loginpage():
   
    return render_template('login.html')
@app.route('/login',methods=['POST'])
def checkuser():
    
    ui=request.form["UserID"]
    pw=request.form["Password"]
    
    mycursor=cnx.cursor()
    query=("select * from Students where StudentID="+str(ui)+" and Password="+str(pw))
    
    mycursor.execute(query)
    res=mycursor.fetchall()
    if len(res)==1:
        session["UserID"]=res[0][0]
        session["StudentName"]=res[0][1]
        user=session["StudentName"]
        return render_template("loggedin.html",sn=res[0][1],uid=res[0][0],smn=res[0][2])
    else:
        return render_template("/login.html",msg="Invalid UserID/Password")
    
@app.route('/register')
def registerpage():
    return render_template('register.html')
@app.route('/register',methods=['POST'])
def insert():
    ui=request.form["userID"]
    pw=request.form["Password"]
    fn=request.form["FullName"]
    mn=request.form["MobileNo"]
    mycursor=cnx.cursor()
    query=("insert into Students(StudentID,StudentName,StudentMobileNo,Password) Values(%s,%s,%s,%s)")
    data=(ui,fn,mn,pw)
    mycursor.execute(query,data)
    cnx.commit()
    return redirect("/Home")

@app.route('/loggedin')
def loggedin():
    if "UserID" in session:
        un=session["StudentName"]
        uid=session["UserID"]
        return render_template("loggedin.html",sn=un,uid=uid)
    else:
        return redirect("/login")
@app.route('/logout')
def logout():
    session.pop('StudentName')
    session.pop('UserID')
    return redirect("/Home") 
@app.route("/mycourses")
def getcourses():
    uid=session["UserID"]
    mycursor=cnx.cursor()
    query=("select c.CourseID,c.CourseName from students s,courses c, studentcourses sc where s.StudentID="+str(uid)+" and s.StudentID=sc.StudentID and c.CourseID=sc.CourseID")  
    mycursor.execute(query)
    mycourses=mycursor.fetchall()

    query=("select * from courses")
    mycursor.execute(query)
    allcourses=mycursor.fetchall()
   
    return render_template("courses.html",currentuser=uid,mycourses=mycourses,mycourseslength=len(mycourses),allcourses=allcourses,allcourseslength=len(allcourses))

@app.route("/<int:userid>/mycourses",methods=["POST"])
def enroll(userid):
    print(str(userid))
    cid=request.form["CourseID"]
    mycursor=cnx.cursor() 
    query=("insert into studentcourses(StudentID,CourseID) Values(%s,%s)")
    data=(userid,cid)
    mycursor.execute(query,data)
    cnx.commit() 
    response={'CourseID':mycursor.lastrowid}
    response=jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route("/test")
def test():
    print(session["UserID"])
    return render_template('testapi.html')
@app.route("/testget",methods=["GET"])
def testget():
    #print(session["UserID"])
    mycursor=cnx.cursor()
    query=("select * from Courses")
    mycursor.execute(query)
    res=mycursor.fetchall()
    response=[]
    for i in res:
        response.append(
            {
                'CourseID':i[0],
                'CourseName':i[1]
            }
        )
    response=jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route("/<x>/testget",methods=["POST"])
def testpost(x):
    print("started")
    print(x)
    a=request.form["CourseID"]
    print(a)
    cursor = cnx.cursor()
    query = ("DELETE FROM courses where CourseID=" + str(a))
    cursor.execute(query)
    cnx.commit()

    return {'CourseID':a}





if __name__=='__main__':
    app.run(debug=True)
    
    

