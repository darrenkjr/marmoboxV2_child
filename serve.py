from flask import render_template, Flask, jsonify, request
import json
import time
import marmobox_control

app = Flask(__name__)
# Create a URL route in our application for "/"
@app.route('/', methods=["GET","POST"])
def main():
    '''
        Calls a trial to be run as per the JSON instruction
    '''
    x = json.loads(request.data)
    marmobox_control.execute_command(x)
    return jsonify(pythonobj)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)

