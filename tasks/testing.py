from psychopy import visual, event
import timeit

mywin = visual.Window([1280, 720], monitor="testMonitor", units="pix", pos=(0, 0))
mouse = event.Mouse(win=mywin)

# control.connect()

black = [-1,-1,-1]
white = [1,1,1]
blue = [-1,-1,1]
red = [1,-1,-1]

lim_trial = 5
trial = 0

centre_grating = visual.GratingStim(win=mywin, size=200, pos=[0, 0], sf=0, color=[-1,-1,-1], colorSpace='rgb')


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


def drawing(centre_grating):
    centre_grating.draw()
    mywin.update

wrapped = wrapper(drawing,centre_grating)
t = timeit.timeit(wrapped, number = 1000)
print(t/1000)