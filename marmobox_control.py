#import classes from arduino control and from tasks - runs declared tasks, pre-import required modules + packages

from psychopy import visual
import importlib
from tasks.helper.json_handler import json_handler
import datetime


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

def __old_main(debug,json_command=None):
    '''
        Main function for marmobox_control.py
    '''
    #load in required tasklist and instructions from json and other paramters (animal_ID etc)
    tasklist, limitTrial, animalID = json_handler.read_input()
    session = 0
    #server url
    json_handler = json_handler()
    url = 'https://ptsv2.com/t/lg7zg-1562113615/post'
    #wait for json input from main marmobox.
    #listen on port & unpack required parameters
    tasklist = ['tasks.touch-training0','tasks.touch-training1']
    animalID = 'test'
    limitTrial = 5

    taskmodule = loadtaskmodule(tasklist)

    trial_response = []
    for i in range(len(tasklist)):
        mywin = visual.Window([1280, 720], monitor="testMonitor", units="pix", pos=(0, 0))
        results = taskmodule[i].run(tasklist[i],limitTrial,mywin,animalID,session) #args = taskname,limitTrial,mywin,animal_ID,session
        timestamp = datetime.datetime.now()
        #send output and results
        json_output = json_handler().create_output(results,animalID,str(timestamp),url)
        trial_response.append(json_output)
        mywin.close()

    #start session counting
    return trial_response

def execute_command(json_command):
    '''
        Main function for marmobox_control.py
    '''
    #load in required tasklist and instructions from json and other paramters (animal_ID etc)
    jsonHandler = json_handler()
    taskname, animalID = jsonHandler.read_input(json_command)
    taskname = 'tasks.screen_latencytest'
    session = 0

    taskmodule = importlib.import_module(taskname)

    print('running ', taskname)
    results = taskmodule.run(taskname,animalID,session) #args = taskname,limitTrial,mywin,animal_ID,session
    timestamp = datetime.datetime.now()
    json_output = jsonHandler.create_json_output(results,animalID,str(timestamp))
    return json_output

if __name__ == "__main__":
    execute_command()