#import classes from arduino control and from tasks - runs declared tasks, pre-import required modules + packages

from psychopy import visual
import importlib
from tasks.helper.json_handler import json_handler
import datetime



#load in required tasklist and instructions from json and other paramters (animal_ID etc)
# tasklist, limitTrial, animalID = json_handler.read_input()
session = 0
#server url
json_handler = json_handler()
url = 'https://ptsv2.com/t/lg7zg-1562113615/post'
#wait for json input from main marmobox.
#listen on port & unpack required parameters


tasklist = ['tasks.touch-training0','tasks.touch-training1']
animalID = 'test'
limitTrial = 5



#loading required tasks, and assigns each task a number
def loadtaskmodule(tasklist):
    taskmodule = []
    for x in tasklist:

        print(x)
        task = importlib.import_module(x)
        taskmodule.append(task)

        print('test')
        print(taskmodule)

    return taskmodule

taskmodule = loadtaskmodule(tasklist)



for i in range(len(tasklist)):
    mywin = visual.Window([1280, 720], monitor="testMonitor", units="pix", pos=(0, 0))
    results = taskmodule[i].run(tasklist[i],limitTrial,mywin,animalID,session) #args = taskname,limitTrial,mywin,animal_ID,session
    timestamp = datetime.datetime.now()
    #send output and results
    json_output = json_handler.create_output(results,animalID,str(timestamp),'https://ptsv2.com/t/lg7zg-1562113615/post')
    mywin.close()

#start session counting


