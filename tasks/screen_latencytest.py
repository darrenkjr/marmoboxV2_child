from psychopy import visual, event
import time, datetime

mywin = visual.Window([1280, 720], monitor="testMonitor", units="pix", pos=(0, 0))
mouse = event.Mouse(win=mywin)


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


    centre_grating.draw()
    top_left_corner.draw()
    print('Drawing!')
    mywin.update()
    reaction_start = datetime.datetime.now()

    #add arduino photodiode class to sync times
    print('Time start. Signaling photodiode sync')

    mouse.clickReset()
    while not mouse.getPressed()[0]:
        #added sleep to prevent premature exit of script
        time.sleep(0.01)

    if mouse.isPressedIn(centre_grating):
        print('Hit')

        reaction_end = datetime.datetime.now()
        # average click takes around 100ms, thus sleep for 0.1s, systems sleeps unresponsive to further clicks
        click_register_timeout = 0.5
        time.sleep(click_register_timeout)




    time_delta = (reaction_end - reaction_start).total_seconds()
    trial += 1
    print('Time between display and touch (software): ',time_delta)


