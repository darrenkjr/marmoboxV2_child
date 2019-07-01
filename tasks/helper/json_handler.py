import json

#take output dictionary, dump into json.

class json_handler:

    def __init__(self):
        print('Initiating json handler. ')


    def read_input(self):
        print('waiting for json signal')


        tasklist = 'placeholder'
        json_string = 'json instructions'

        return tasklist, json_string

    def create_output(self,results,animal_ID,timestamp):
        # take in raw data, put into dictionary

        print('creating json output for sending to central server. ')

        #creating dictionary
        json_out_dict = {
            'results' : results, 'Animal ID' : animal_ID, 'timestamp' : timestamp
        }

        json_out_string = json.dumps(json_out_dict)

        #send json to server / datawarehouse
