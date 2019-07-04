from flask import render_template, Flask, jsonify, request
import json
import time
import marmobox_control
import multiprocessing as mp
import os

mp.set_start_method('spawn')
q = mp.Queue()
p = mp.process
app = Flask(__name__)
# Create a URL route in our application for "/"
@app.route('/', methods=["GET","POST"])
def main():
    '''
        Calls a trial to be run as per the JSON instruction
    '''
    json_string = request.data
    marmobox_control.execute_command(json_string)
    return jsonify(pythonobj)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)

