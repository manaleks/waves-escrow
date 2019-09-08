import os
import sys

from flask import Flask
from flask import Response
from flask import request, session, abort
from flask import redirect
from flask import render_template
from flask import jsonify


import requests


import pywaves as pw


# app = Flask(__name__) # to make the app run without any
app = Flask(__name__)
app.secret_key = os.urandom(12)
# SERV
@app.route('/', methods=['GET', 'POST'])
def server_work():
    if request.method == 'POST':
        pass
    if 'user' in session.keys():
        return render_template('index.html')
    else:
        return render_template('signup.html')
@app.route('/home', methods=['GET', 'POST'])
def index_work():
    if request.method == 'POST':
        pass
    return render_template('index.html')
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        pass
    return render_template('new.html')
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



@app.route("/signin", methods = ['POST'])
def Authenticate():
    username = request.args.get('email')
    password = request.args.get('password')
    session['user'] = '{id : 1}'
    return jsonify({'success':1})


@app.route("/signup", methods = ['POST'])
def Sigunp():
    username = request.args.get('email')
    address = request.args.get('adress')
    password = request.args.get('password')
    session['user'] = '{id : 1}'
    return jsonify({'success':1})


if __name__ == "__main__":
    app.run(debug=True, port=5000)

