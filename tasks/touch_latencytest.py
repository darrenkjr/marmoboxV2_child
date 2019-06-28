from psychopy import visual, event
import time, datetime
import numpy as np


mywin = visual.Window([1280, 720], monitor="testMonitor", units="pix", pos=(0, 0))
grating = visual.GratingStim(win=mywin, size=700, pos=[0,0], sf=0, color = [-1,-1,1], colorSpace='rgb')
mouse = event.Mouse(win=mywin)


grating.draw()
mywin.update()

mouse.clickReset()
counter = 0

while not mouse.getPressed()[0]:
	time.sleep(0.0001)

if mouse.isPressedIn(grating) == True:
	start_time = datetime.datetime.now()
	x_coord = []
	y_coord = []
	while mouse.isPressedIn(grating):

		counter +=1
		print(counter)
		x_coord.append(mouse.getPos()[0])
		y_coord.append(mouse.getPos()[1])

if counter >1:
	end_time = datetime.datetime.now()
	time_delta = (end_time - start_time).total_seconds()
	print((time_delta))
	coord = [x_coord,y_coord]

print(counter,time_delta)
uniques, counts = np.unique(coord,return_counts = True)
print(uniques, counts)
sample_rate = counter / time_delta

print('Sample rate (per second): ', sample_rate)

