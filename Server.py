
from SqlConnection import getSqlConnection
from flask import Flask,jsonify,request
import Students_dao
import json

app = Flask(__name__)
Connection=getSqlConnection()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/Students', methods=['GET'])
def getAllStudents():
    S=Students_dao.getAllStudents(Connection)
    response=jsonify(S)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route('/insertStudent', methods=['POST'])
def insertNewStudent():
    request_payload=json.loads(request.form["data"])
    StudentID=Students_dao.insertNewStudent(Connection,request_payload)
    response = jsonify({
        'StudentID': StudentID
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/getStudent', methods=['POST']) 
def getStudent():
    request_payload=json.loads(request.form["data"])
    Student=Students_dao.getStudent(Connection,request_payload)
    response = jsonify(Student)
    return response

    
if __name__=='__main__':
    app.run(debug=True)
