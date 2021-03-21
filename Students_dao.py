import mysql.connector
from SqlConnection import getSqlConnection
def getAllStudents(cnx):
    
    
    mycursor = cnx.cursor()

    mycursor.execute("SELECT StudentID,StudentName,StudentMobileNo FROM Students")
    response=[]
    for (StudentID,StudentName,StudentMobileNo) in mycursor:
        response.append(
            {'StudentID':StudentID, 'StudentName':StudentName, 'StudentMobileNo':StudentMobileNo}
            )
    return response
    myresult = mycursor.fetchall()

   
def insertNewStudent(cnx,Student):
    mycursor=cnx.cursor()
    query=("insert into Students(StudentID,StudentName,StudentMobileNo,Password) Values(%s,%s,%s,%s)")
    data=(Student["StudentID"],Student["StudentName"],Student["StudentMobileNo"],Student["Password"])
    mycursor.execute(query,data)
    cnx.commit()
    return mycursor.lastrowid


def getStudent(cnx,data):
    userid=data["StudentID"]
    password=data["Password"]
    mycursor = cnx.cursor()

    mycursor.execute("SELECT * FROM Students where StudentID="+str(userid)+" and Password="+str(password))
    res=mycursor.fetchall()
    response=[]
    for i in res:
        response.append(
            {
                'StudentID':i[0],
                'StudentName':i[1],
                'StudentMobileNo':i[2]
                
            }
        )
    return response



if __name__=='__main__':
    Connection=getSqlConnection()
    print(getAllStudents(Connection))
    print(getStudent(Connection,{'StudentID':2,'Password':'123'}))
    
    
    
