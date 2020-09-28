#!/usr/bin/env python3

from flask import Flask,render_template,request

import config

from led_functions import set_color,init

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('buttonpage.html', functions=['clear','rainbow','all_green','all_red','all_blue'])
    
@app.route('/', methods=['POST'])
def parse_request():
    data = request.form
    function = data.get('function')
    
    if function == 'clear':
        set_color(0,0,0)
    elif function == 'all_blue':
        set_color(0,255,0)
    elif function == 'all_red':
        set_color(255,0,0)
    elif function == 'all_green':
        set_color(0,0,255)
    return index()
    
if __name__ == '__main__':
    init()
    app.run(debug=True, port=80, host='0.0.0.0')
