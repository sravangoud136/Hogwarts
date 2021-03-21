from flask import Flask,jsonify,request,redirect,render_template
import os
app = Flask(__name__)
#Connection=getSqlConnection()
uploadpath="\static\Files"
@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/uploader')
def uploadhome():
    
    return render_template("testapi.html")
@app.route('/uploader',methods=["POST"])
def uploadfile():
    if request.method=="POST":
        if request.files:
            filedata=request.files["profilepic"]
            filedata.save(os.path.join("d:\\NodeLearn\\Hogwarts\\Hogwarts\\Backend\\static\\Files",filedata.filename))
            print("image uploaded")
            
    return render_template("testapi.html",status="File Uploaded successfully")


if __name__=='__main__':
    print("started"+os.path.dirname("shri-krishna.jpg"))
    #print(os.path.abspath(os.path.join(os.path.dirname("shri-krishna.jpg"), os.path.pardir)))
    app.run(debug=True)
