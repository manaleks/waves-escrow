import os
import sys

from flask import Flask
from flask import Response
from flask import request
from flask import redirect
from flask import render_template

import requests



app = Flask(__name__)


# SERV
@app.route('/', methods=['GET', 'POST'])
def server_work():
    if request.method == 'POST':
        pass
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

