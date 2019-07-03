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
top_left_corner = visual.GratingStim(win=mywin, size=20, pos=[-(1280 / 2) + 20, (720 / 2) - 20], sf=0, color=[1,-1,1],
                                         colorSpace='rgb')

def wrapper(func, *args):
    def wrapped():
        return func(*args)

    return wrapped


def drawing(centre_grating,top_left_corner):
    mywin
    centre_grating.draw()
    top_left_corner.draw()
    mywin.update()
    print('test')


wrapped = wrapper(drawing,centre_grating, top_left_corner)

t = timeit.timeit(wrapped, number = 1000)
mywin.close()
print(t/1000)