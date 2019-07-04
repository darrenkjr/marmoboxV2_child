from psychopy import visual, event
import time, datetime
import timeit
# from arduinocontrol import arduino_control as control

mywin = visual.Window([1280, 720], monitor="testMonitor", units="pix", pos=(0, 0))
mouse = event.Mouse(win=mywin)

# control.connect()

black = [-1,-1,-1]
white = [1,1,1]
blue = [-1,-1,1]
red = [1,-1,-1]

lim_trial = 5
trial = 0



while trial <= lim_trial:
    if trial%2 == 0:
        color = white
        centre_color = blue
    else:
        color = black
        centre_color = red

    top_left_corner = visual.GratingStim(win=mywin, size=20, pos=[-(1280 / 2) + 20, (720 / 2) - 20], sf=0, color=color,
                                         colorSpace='rgb')
    centre_grating = visual.GratingStim(win=mywin, size=200, pos=[0, 0], sf=0, color=centre_color, colorSpace='rgb')


    top_left_corner.draw()
    centre_grating.draw()

    print('Drawing!')
    mywin.update()
    screen_refresh = datetime.datetime.now()

    #add arduino photodiode class to sync times
    print('Time start. Signaling photodiode sync')


    mouse.clickReset()
    while not mouse.getPressed()[0]:
        #added sleep to prevent premature exit of script
        time.sleep(0.01)

    if mouse.isPressedIn(centre_grating):
        initial_touch = datetime.datetime.now()
        print('Hit')
        while mouse.isPressedIn(centre_grating) is True:
            print('Touch~~~')

        time_release = datetime.datetime.now()

    reaction_latency = (initial_touch - screen_refresh).total_seconds()
    time_held = (time_release - initial_touch).total_seconds()
    trial += 1
    print('Time between display and touch (software): ',reaction_latency)
    print('Time of holding.', time_held)


