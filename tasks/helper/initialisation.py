from psychopy import event
import time


def initial_param(mywin):
    mouse = event.Mouse(win=mywin)
    trial = 0
    nulls = 0
    timer = time.time()
    xpos = 0
    ypos = 0
    touchTimeout = False
    correct = []
    wrong = []
    hits = 0
    null = 0
    miss = 0
    results = []
    summary = []

    return mouse, trial,nulls,timer,xpos,ypos, touchTimeout,correct,wrong,hits,null, miss, results, summary




