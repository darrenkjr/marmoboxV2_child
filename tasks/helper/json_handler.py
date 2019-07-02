import json

#take output dictionary, dump into json.

class json_handler:

    def __init__(self):
        print('Initiating json handler. ')


    def read_input(self,json_string):
        print('waiting for json signal')


        tasklist = 'placeholder'
        json_string = 'json instructions'

        #unpack json
        limitTrial = 'placeholder'
        animalID = 'placeholder '

        return tasklist, limitTrial, animalID

    def create_output(self,results,animal_ID,timestamp):
        # take in raw data, put into dictionary

        print('creating json output for sending to central server. ')

        #creating dictionary
        json_out_dict = {
            'results' : results, 'Animal ID' : animal_ID, 'timestamp' : timestamp
        }

        json_out_string = json.dumps(json_out_dict)

        #send json to server / datawarehouse
