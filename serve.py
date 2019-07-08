from flask import render_template, Flask, jsonify, request
import json
import time
import marmobox_control
# from multiprocessing import Process
import multiprocessing as mp
import os
def command(json_string,return_val):
    return_val = marmobox_control.execute_command(json_string)

app = Flask(__name__)
# Create a URL route in our application for "/"
@app.route('/', methods=["GET","POST"])
def main():
    '''
        Calls a trial to be run as per the JSON instruction
    '''
    json_string = request.data
    manager = mp.Manager()
    return_val = manager.list()
    p = mp.Process(target=command, args=(json_string,return_val))
    p.start()
    p.join()
    return jsonify({})

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    mp.set_start_method('spawn')
    app.run(debug=True)

