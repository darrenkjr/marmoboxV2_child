from psychopy import visual, core
import time, datetime
from tasks.helper.initialisation import initial_param
from libraries import arduinocontrol as control

''' touchtraining script for marmobox. Takes in instructions as json files and executes according to progression level'''

def run(mywin,instructions):
	mouse, trial, nulls, timer, xpos, ypos, touchTimeout, correct, wrong, hits, null, miss, results, summary = initial_param(mywin)

	#unpack instructions from json dict
	print(instructions)
	stim_size, color, stim_coord, time_penalty = instructions['Stimulus size'],instructions['Stimulus color'],instructions['Stimulus coordinates'],instructions['ITI for Wrong Response']
	#stim type = size of stimulus + rgb code
	stim_s = stim_size
	stim_type = str(stim_s+color)

	#create #blue stimulus
	print(stim_size)
	grating = visual.GratingStim(win=mywin, size=stim_size, pos=stim_coord, sf=0, color=color, colorSpace='rgb' )
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
		results += [screen_refresh.strftime("%H:%M %p"), xpos, ypos, stim_type, stim_coord, reaction_latency, time_held, 1,
							hits, miss, null]

	else:
		initial_touch = datetime.datetime.now()
		xpos, ypos = mouse.getPos()[0], mouse.getPos()[1]  # Returns current positions of mouse during press
		print('Miss!')

		# trigger penalty
		# control.wrong()
		core.wait(time_penalty)
		miss+=1

		while mouse.isPressedIn(grating):
			time.sleep(0.001)  # smaller inteval than actual screen refresh rate and touch sample rate
		time_release = datetime.datetime.now()

		reaction_latency = (initial_touch - screen_refresh).total_seconds()
		time_held = (time_release - initial_touch).total_seconds()
		# results for this session, 1 = success, 0 = fail
		results += results + [screen_refresh.strftime("%H:%M %p"), xpos, ypos, stim_type, stim_coord, reaction_latency, time_held, 0, hits, miss, null]

	trial_end = str(datetime.datetime.now())
	results += [trial_end]
	print(results)
	return results

	
	
	
	
	


