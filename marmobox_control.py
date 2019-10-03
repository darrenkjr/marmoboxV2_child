#import classes from arduino control and from tasks - runs declared tasks, pre-import required modules + packages
from psychopy import visual, core
import importlib
from tasks.helper.json_handler import json_handler
import multiprocessing as mp
from flask import render_template, Flask, jsonify, request
import json
from libraries.reward_penalty_control import reward


def execute_command(q_in,q_out):
    '''
        Main function for marmobox_control.py
    '''
    mywin = visual.Window([1280, 720], monitor="testMonitor", units="pix", pos=(0, 0))


    while True:
        #while script is running, listen for get requqests from server.
        json_command = q_in.get()
        # load in required tasklist and instructions from json and other paramters (animal_ID etc)
        jsonHandler = json_handler()
        taskname, animalID,  level, instructions = jsonHandler.read_input(json_command)
        taskmodule = importlib.import_module(taskname)

        print('running ', taskname, level)
        print(instructions)
        results = taskmodule.run(mywin,instructions) #args = taskname,limitTrial,mywin,animal_ID,session, instructions (dictionary)
        print(results)
        json_output = jsonHandler.create_json_output(results) #results, is a list
        q_out.put(json_output)
        mywin.update()

    mywin.close()

def loadtaskmodule(tasklist):
    '''
        loading required tasks, and assigns each task a number
    '''
    taskmodule = []
    for x in tasklist:
        print(x)
        task = importlib.import_module(x)
        taskmodule.append(task)
        print('test')
        print(taskmodule)

    return taskmodule

# Create a URL route in our application for "/"
if __name__ == "__main__":
    mp.set_start_method('spawn')
    q_in = mp.Queue()
    q_out = mp.Queue()
app = Flask(__name__)
# Create a URL route in our application for "/"

@app.route('/', methods=["GET","POST"])
def main():
    '''
        Calls a trial to be run as per the JSON instruction
    '''
    json_string = request.data
    q_in.put(json_string)
    out = q_out.get()
    json_out = json.dumps(out)
    print(json_out)
    return json_out

if __name__ == "__main__":
    # json_command = '{"taskname":"tasks.touch-training0","animal_ID":"test"}'
    # q_in.put(json_command)
    p = mp.Process(target=execute_command, args=(q_in,q_out))
    p.start()
    server_address = ('', 8000)
    httpd = HTTPServer(server_address,BaseHTTPRequestHandler)
    httpd.serve_forever()
    app.run(debug=True)
    p.join()
