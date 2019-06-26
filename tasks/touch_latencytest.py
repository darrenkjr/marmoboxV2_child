from psychopy import visual, event
import time, datetime


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
	start_time = time.time()
	while mouse.isPressedIn(grating):

		counter +=1
		print(counter)

if counter >1:
	time_delta = (time.time() - start_time)
	print((time_delta))
	sample_rate = counter / time_delta

print('Sample rate (per second): ', sample_rate)

