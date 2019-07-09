from psychopy import visual, core
import time, datetime
from tasks.helper.initialisation import initial_param
from libraries import arduinocontrol as control



def run(mywin,instructions):
	mouse, trial, nulls, timer, xpos, ypos, touchTimeout, correct, wrong, hits, null, miss, results, summary = initial_param(mywin)

	#unpack instructions from json dict
	print(instructions)
	stim_size, color, stim_coord, time_penalty = instructions.values()

	#create #blue stimulus
	grating = visual.GratingStim(win=mywin, size=stim_size, pos=stim_coord, sf=0, color = color, colorSpace='rgb' )
	grating.draw()
	print('Drawing!')
	mywin.update()
	#start reaction timer from drawing the grating. Also defines trial start.
	screen_refresh = datetime.datetime.now()

	mouse.clickReset() #resets a timer for timing button clicks


	while not mouse.getPressed()[0]:# checks whether mouse button (i.e. button '0') was pressed
		time.sleep(0.01) # #added sleep to prevent premature exit of script

	if mouse.isPressedIn(grating):
		initial_touch = datetime.datetime.now()
		xpos, ypos = mouse.getPos()[0], mouse.getPos()[1]  # Returns current positions of mouse during press
		print('Hit!')
		#trigger reward (implement arduino)
		# control.correct()

		#do this from server
		time_stamp = datetime.datetime.now().strftime("%H:%M %p")

		print(results)
		hits += 1

		while mouse.isPressedIn(grating):
			time.sleep(0.001) #smaller inteval than actual screen refresh rate
		time_release = datetime.datetime.now()

		reaction_latency = (initial_touch - screen_refresh).total_seconds()
		time_held = (time_release - initial_touch).total_seconds()
		#results for this session, 1 = success, 0 = fail
		results.append([time_stamp,xpos,ypos,stim_coord,reaction_latency, time_held, 1, hits,miss,null])

	else:
		initial_touch = datetime.datetime.now()
		xpos, ypos = mouse.getPos()[0], mouse.getPos()[1]  # Returns current positions of mouse during press
		print('Miss!')

		# trigger penalty
		# control.wrong()
		core.wait(time_penalty)


		print(results)
		miss+=1

		while mouse.isPressedIn(grating):
			time.sleep(0.001)  # smaller inteval than actual screen refresh rate and touch sample rate
		time_release = datetime.datetime.now()

		reaction_latency = (initial_touch - screen_refresh).total_seconds()
		time_held = (time_release - initial_touch).total_seconds()
		# results for this session, 1 = success, 0 = fail
		results.append([screen_refresh.strftime("%H:%M %p"), xpos, ypos, stim_coord, reaction_latency, time_held, 0, hits, miss, null])


	time_end = datetime.datetime.now().strftime("%H:%M %p")
	results.append(time_end)
	print(results)
	return results

	
	
	
	
	


