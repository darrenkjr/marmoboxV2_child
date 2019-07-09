import json
import requests

#take output dictionary, dump into json.

class json_handler:

    def __init__(self):
        print('Initiating json handler. ')


    def read_input(self,json_string):
        '''
            Reads JSON command and returns output tasklist, limitTrial, animalID
        '''
        # task = 'tasks.touch-training0'
        # animalID = 'F1234_test'
        print('waiting for json signal')
        print(json_string)
        json_string = json.loads(json.loads(json_string.decode('utf-8')))
        print(json_string, type(json_string))

        # taskname = json_string.task if 'taskname' in json_string else 'default'
        taskname = json_string.get('taskname')
        print(taskname)
        # animalID = json_string.animal_ID if 'animal_ID' in json_string else 'F1234_test'
        animalID = json_string.get('animal_ID')
        print(animalID)
        #get instructions (task specific)
        instructions = json_string.get('instructions')
        level = json_string.get('level')
        return taskname, animalID, level, instructions

    def create_json_output(self,results,animal_ID,timestamp):
        json_out_dict = {
            'results': results, 'Animal ID': animal_ID, 'timestamp': timestamp
        }
        return  json_out_dict

    def create_output(self,results,animal_ID,timestamp,url):
        # take in raw data, put into dictionary

        print('creating json output for sending to central server. ')

        #creating dictionary
        json_out_dict = {
            'results' : results, 'Animal ID' : animal_ID, 'timestamp' : timestamp
        }

        json_out_string = json.dumps(json_out_dict)
        #send json to server / datawarehouse
        requests.post(url,json_out_string)
        return json_out_dict

