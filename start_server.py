#!/usr/bin/env python3

from flask import Flask,render_template,request

import config

import webcolors

#from led_functions import set_color,init,set_rainbow_color

app = Flask(__name__)
#init()

def name_to_rgb(color):
    color = webcolors.name_to_rgb(color)
    return color.red,color.green,color.blue


def hex_to_rgb(color):
    color = webcolors.hex_to_rgb(color)
    return color.red,color.green,color.blue

functions=['clear','rainbow','all_green','all_red','all_blue','all_pink','all_white']

def write_tempfile(function):
    f = open(config.tempfile_path, 'w')
    f.write(function)
    f.close()

@app.route('/', methods=['GET'])
def index(color='#FFFFFF'):
    return render_template('buttonpage.html', functions=functions,last_color=color)
    
@app.route('/', methods=['POST'])
def parse_request():
    data = request.form
    function = data.get('function')
    
    
    if function in functions:
        write_tempfile(function)
    if function == 'colorpick':
        try:
            color = data.get('color')
            red, green, blue = hex_to_rgb(color)
            write_tempfile('colorpick:{}:{}:{}'.format(red,green,blue))
            return index(color)
        except ValueError:
            pass
    if function == 'colorname':
        try:
            color = data.get('color')
            red, green, blue = name_to_rgb(color)
            write_tempfile('colorpick:{}:{}:{}'.format(red,green,blue))
            return index(color)
        except ValueError:
            pass
        except Exception as e:
            return str(e)
    return index()

api_functions=['all','colorpicker']

@app.route('/api/<function>/<color>',methods=['POST'])
def api(function,color):
{
    if function not in api_functions:
        return False
    if function == 'colorpick':
        try:
            red, green, blue = hex_to_rgb(color)
            write_tempfile('colorpick:{}:{}:{}'.format(red,green,blue))
            return index(color)
        except ValueError:
            return False
    elif function == 'all':
        red, green, blue = name_to_rgb(color)
        write_tempfile('colorpick:{}:{}:{}'.format(red,green,blue))
        return index(color)
    return True
}
    
if __name__ == '__main__':
    
    app.run(debug=True, port=80, host='0.0.0.0')
