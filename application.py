import os
import sys

from flask import Flask
from flask import Response
from flask import request
from flask import redirect
from flask import render_template
from flask import jsonify
from flaskext.mysql import MySQL
import hashlib

import requests


import pywaves as pw

mysql = MySQL()

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# SERV
@app.route('/', methods=['GET', 'POST'])
def server_work():
    if request.method == 'POST':
        pass
    return render_template('signup.html')

@app.route('/waves', methods=['GET', 'POST'])
def waves():
    if request.method == 'POST':
        pass

    myAddress = pw.Address(privateKey='4GXSoZdGi8bgkC98H8FpNZ5kjv92s8YASRsbNWXU7hVt')
    print(1)
    otherAddress = pw.Address('3NCcsyMn1R9feUBBnFCTBaVcWD2LKq4ErfG')
    print(2)
    myAddress.sendWaves(otherAddress, 10000)
    print(3)
    myToken = myAddress.issueAsset('Token1', 'My Token', 1000, 0)
    print(4)
    while not myToken.status():
        pass
    print(5)
    myAddress.sendAsset(otherAddress, myToken, 50)

    return 'ok'


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'john', '2':'steve', '3':'bill'}
    
    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()



@app.route("/login", methods = ['POST'])
def Authenticate():
    username = request.args.get('email')
    password = request.args.get('password')
    if username and password:
        password = hashlib.md5(password.encode()).hexdigest()
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from user where email='" + username + "' and pass='" + password + "'")
        data = cursor.fetchone()
        if data is None:
         return "Username or Password is wrong"
    else:
     return "Logged in successfully"


@app.route("/signup", methods = ['POST'])
def Sigunp():
    username = request.args.get('email')
    address = request.args.get('adress')
    password = request.args.get('password')
    if username and address and password:
        password = hashlib.md5(password.encode()).hexdigest()
        cursor = mysql.connect().cursor()
        cursor.execute("INSERT INTO user VALUES(NULL,'" + username + "','" + address + "','" + password + "',NOW()")
        mysql.connect().commit()
    else:
        return jsonify({'error':'fill all the form'})







if __name__ == "__main__":
    app.run(debug=True, port=5000)

