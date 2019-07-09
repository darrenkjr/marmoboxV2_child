# from libraries.audio import tone
from libraries.arduinocontrol import arduino_control as control

class reward():
    def __init__(self):
        arduino = control()
    def correct(self):
        tone(800, 1, 0.5)
        # control.
        #pump according to progressive ratios
        x = 'placeholder'

    def wrong(self):
        tone(330,1,0.5)
        #no pump

