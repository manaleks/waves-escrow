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
app.config['SESSION_TYPE'] = 'filesystem'

users = [{'id': 1,
    'firstname': "Default", 
    'lastname': "User", 
    'email': "mail@user.com", 
    'password': "pass", 
    'publicKey': "09HGUhhkjjk98098"
    },
    {'id': 2,
    'firstname': "Default2", 
    'lastname': "User2", 
    'email': "mail2@user.com", 
    'password': "pass", 
    'publicKey': "09HGUhhkjjk98098"
    },
]
deals = [{
    'id': 1,
    'sender': 1, 
    'receiver': 2,
    'deadline':'name..',
    'description':'condition',
    'amount':10000000, 
    'status': 1
    },
    {
    'id': 2,
    'sender': 1, 
    'receiver': 2,
    'deadline':'name..',
    'description':'condition',
    'amount':10000000, 
    'status': 1
    }
]
nextId = len(users) + 1

def verifySessionId():
    global nextId
    if not 'userId' in session:
        session['userId'] = nextId
        nextId += 1
        sessionId = session['userId']
        print ("set userid[" + str(session['userId']) + "]")
    else:
        print ("using already set userid[" + str(session['userId']) + "]")
    sessionId = session.get('userId', None)
    return sessionId
def getUserById(id):
    global users
    for user in users:
        if user['id'] == verifySessionId():
            return user


@app.route('/home_owner', methods=['GET', 'POST'])
def home_owner():
    if request.method == 'POST':
        return render_template('index.html', deals = deals)
    else:
        return render_template('home_owner.html')


@app.route('/', methods=['GET', 'POST'])
def server_work():
    global deals
    if request.method == 'POST':
        pass
    if 'user' in session.keys():
        for deal in deals:
            sender = getUserById(deal['sender'])
            deal['sender_name'] = sender['firstname'] + ' ' + sender['lastname']
            _deals.append(deal)
        return render_template('index.html', deals = _deals, user = getUserById(verifySessionId()))
    else:
        return render_template('signup.html')

@app.route('/home', methods=['GET', 'POST'])
def index_work():
    global deals
    if request.method == 'POST':
        pass
    _deals = []
    for deal in deals:
        sender = getUserById(deal['sender'])
        if sender is not None :
            deal['sender_name'] = sender['firstname'] + ' ' + sender['lastname']
        else:
            deal['sender_name'] = "Sender " + deal['sender']
        _deals.append(deal)
    return render_template('index.html', deals = _deals, user = getUserById(verifySessionId()))

@app.route('/new', methods=['GET', 'POST'])
def new():
    global users
    if request.method == 'POST':
        pass
    return render_template('new.html', user = getUserById(verifySessionId()), users = users)


@app.route('/viewdeal/<int:dealid>', methods=['GET', 'POST'])
def viewdeal(dealid):
    global deals
    if request.method == 'POST':
        pass
    for deal in deals:
        if dealid == deal['id']:
            return render_template('viewdeal.html', deal = deal, user = getUserById(verifySessionId()), address = getUserById(deal['sender'])['publicKey'])
    else:
        return not_found()

#Сделка ... 
@app.route('/newdeal', methods=['POST'])
def newdeal():
    global deals
    description = request.form['description']
    amount = request.form['amount']
    receiver = request.form['receiver']
    deadline = request.form['deadline']
    deals.append({
    'id': len(deals) + 1,
    'sender': verifySessionId(), 
    'receiver': receiver,
    'deadline':deadline,
    'description': description,
    'amount':amount, 
    'status': 1
    })
    return jsonify({'success':1})

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
    global users 
    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()

@app.route('/deal/<dealid>', methods = ['GET'])
def api_deals(dealid):
    global deals
    if dealid in deals:
        return jsonify({dealid:deals[dealid]})
    else:
        return not_found()


@app.route("/signin", methods = ['POST'])
def Authenticate():
    global users
    email = request.form['email']
    password = request.form['password']
    userId = verifySessionId()
    print("User id[" + str(userId) + "]")
    
    for user in users:
        if user['email'] == email and user['password'] == password:
            session['user'] = user
            return jsonify({'success':1})
    return jsonify({'success':0, 'message': "Failed"})

@app.route("/signup", methods = ['POST'])
def Sigunp():
    global users
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    address = request.form['address']
    users.append({
        'id': verifySessionId(),
    'firstname': firstname, 
    'lastname': lastname, 
    'email': email, 
    'password': password, 
    'publicKey': address
    })
    print("User id[" + str(verifySessionId()) + "]")
    session['user'] = getUserById(verifySessionId())
    return jsonify({'success':1})


if __name__ == "__main__":
    app.run(debug=True, port=5000)

