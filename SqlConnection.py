import mysql.connector
__cnx=None
def getSqlConnection():
    global __cnx
    if __cnx is None:
        cnx = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="hogwarts"
        )
    return cnx
