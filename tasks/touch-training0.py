from psychopy import visual, core, logging, event
import time, datetime
from tasks.helper.initialisation import initial_param
from libraries import arduinocontrol as control
import pandas as pd



def run(taskname, animal_ID,session):
	mywin = visual.Window([1280, 720], monitor="testMonitor", units="pix", pos=(0, 0))
	mouse, trial, nulls, timer, xpos, ypos, touchTimeout, correct, wrong, hits, null, miss, results, summary = initial_param(mywin)

	print('debug message')
	#dummies
	stimPosx = 0
	stimPosy = 0
	stim_size = (1280,720)

	#create #blue stimulus
	grating = visual.GratingStim(win=mywin, size=stim_size, pos=[stimPosx,stimPosy], sf=0, color = [-1,-1,1], colorSpace='rgb' )

	limitTrial = 5
	while trial < limitTrial:

		t=time.time() #returns time in sec as float

		grating.draw()
		mywin.update()
		stimuli_presentation = datetime.datetime.now()
		mouse.clickReset() #resets a timer for timing button clicks

		# start reaction timer from drawing the grating

		while not mouse.getPressed()[0]:# checks whether mouse button (i.e. button '0') was pressed
			time.sleep(0.01) # Sleeps if not pressed and then checks again after 10ms


		if mouse.isPressedIn(grating):
			print('Hit!')
			initial_touch = datetime.datetime.now()
			time.sleep(0.15)
			xpos = mouse.getPos()[0] #Returns current positions of mouse during press
			ypos = mouse.getPos()[1]
			buttons = True #Returns True if mouse pressed in grating

			dist_stim = ((stimPosx - xpos) ** 2 + (stimPosy - ypos) ** 2) ** (1 / 2.0)
			session_time = datetime.datetime.now().strftime("%H:%M %p")
			reaction_time = (initial_touch - stimuli_presentation).total_seconds()
			results.append([session,session_time,trial, xpos, ypos, time.time() - t, '-', dist_stim, reaction_time])
			print(results)
			hits += 1

		else:
			print('miss! ')
			initial_touch = datetime.datetime.now()

			#longer penalty for wrong touch
			time.sleep(0.5)

			xpos = mouse.getPos()[0]  # Returns current positions of mouse during press
			ypos = mouse.getPos()[1]
			buttons = False

			dist_stim = ((stimPosx - xpos) ** 2 + (stimPosy - ypos) ** 2) ** (1 / 2.0)
			session_time = datetime.datetime.now().strftime("%H:%M %p")
			reaction_time = (initial_touch - stimuli_presentation).total_seconds()
			results.append([session, session_time, trial, xpos, ypos, time.time() - t, '-', dist_stim, reaction_time])
			print(results)
			miss += 1


		trial += 1
		print(trial)
		mywin.close()

	return results


    # Timer variables
	totalTime = time.time() - timer
	mins = int(totalTime / 60)
	secs = round((totalTime % 60), 1)
	timeLog = str(mins) + ' min ' + str(secs) + ' sec'






	#
	# df_results = pd.DataFrame(results, columns=results_col)
	# reportobj_trial.writecsv('trial',session)
	# average_dist = float(df_results[['Distance from stimulus center (Px)']].mean())
	# avg_reactiontime = float(df_results[['Reaction time (s)']].mean())
	#
	# session_time = datetime.datetime.now().strftime("%H:%M %p")
	# summary.append([session,session_time, timeLog, limitTrial, average_dist, avg_reactiontime])
	# sucess = (float(hits) / float(limitTrial)) * 100
	# reportobj_summary.addEvent(summary)
	# reportobj_summary.writecsv('summary',session)
	#
    # # organizing coordinates
	# pressed = ([df_results['X-Position (Pressed)']], [df_results['Y-Position (Pressed)']])
	# stimulus = (0,0)
	# # creating scatter object and saving heat map plot
	# scatter = scatterplot(stimulus, pressed, stim_size)
	# scatter.heatmap_param(limitTrial, stim_size)
	# scatter.saveheatmap(taskname, animal_ID, limitTrial)
	#
	return totalTime
	
	
	
	
	
	


