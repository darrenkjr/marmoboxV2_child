#classes associated with behaviour reinforcement and reward dispensing systems, and correct + incorrect classes
import serial #Requires pyserial - pip install pyserial
import time

class arduino_control:
    def __init__(self):
        print("Setup Arduino")
        self.connect()
        self.debug = False
        return
    
    def connect(self):
        '''
        Initiate Uart Connection
        '''
        self.pump_arduino = serial.Serial('/dev/ttyACM0',9600,timeout=1)
        #note that aruduino restarts on serial connection
        time.sleep(0.5) #ensure that arduino has started before proceeding
        return

    def disconnect(self):
        '''
        Disconnect from uart
        '''
        self.pump_arduino.close()
        return
    
    def set_debug(self,val):
        '''
        Set debug val as true or false
        Debug enables print statments in the arduino_control class
        '''
        self.debug = val
        return

    def pump(self,volume):
        ''' Dispenses a set (volume) from the pump'''
        # Run pump
        time = self.volume_to_time(volume)
        self.pump_arduino.write(bytes('M{millis}\r'.format(millis=time),'utf-8'))
        if self.debug:
            print("Dispensed {volume} microlitres in {time} ms \n".format(volume=volume,time=time))
        return 

    def volume_to_time(self,volume):
        '''volume in uL (micro litres) return: time in milliseconds that the pump is on'''
        # Function that maps volume to time
        time = volume * 1.75 # uL/ms
        return time


class arduino_screen_calibration:
    def __init__(self):
        self.connect()
        return
    def connect(self):
        '''
        Initiate Uart Connection
        '''
        self.calib = serial.Serial('/dev/ttyACM0',115200,timeout=1)
        #note that aruduino restarts on serial connection
        time.sleep(0.5) #ensure that arduino has started before proceeding
        return

    def disconnect(self):
        '''
        Disconnect from uart
        '''
        self.calib.close()
        return
    def start_timer(self):

        return

    def read_timer(self,sleep_time=1):
        timer_value = 0
        #read delta time back from arduino on UART
        time.sleep(sleep_time) # Need to wait for the screen to change
        timer_value = self.calib.readline()
        return timer_value