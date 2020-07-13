#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Fri Jul  3 15:48:23 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random as rdm

from psychopy.hardware import keyboard

#from data_recv_wired import DataReceiver
#from data_recv_wireless import WiFiDataReceiver




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'Experimento'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Applications/Documentos/Experimentos/attenti/main/Experimento0.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Pelicula/episodio random
pelis=['/Applications/Documentos/Experimentos/videos/HIMYMS02E03.mkv','/Applications/Documentos/Experimentos/videos/HIMYMS02E21.mkv','/Applications/Documentos/Experimentos/videos/HIMYMS03E09.mkv']
cap=rdm.choice(pelis)

# Initialize components for Routine "trial"
trialClock = core.Clock()
movie = visual.MovieStim3(
    win=win, name='movie',
    noAudio = False,
    filename=cap,
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=0.0,
    )
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)
noise = visual.NoiseStim(
    win=win, name='noise',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=0.95, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=0.0625, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-2.0)
noise.buildNoise()
sound_2 = sound.Sound('C', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1)
noise_2 = visual.NoiseStim(
    win=win, name='noise_2',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=0.95, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=0.0625, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-4.0)
noise_2.buildNoise()
sound_3 = sound.Sound('D', secs=-1, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1)
noise_3 = visual.NoiseStim(
    win=win, name='noise_3',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=0.95, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=0.0625, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-6.0)
noise_3.buildNoise()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(1290.000000)
    # update component parameters for each repeat
    sound_1.setSound('A', secs=5, hamming=True)
    sound_1.setVolume(1, log=False)
    sound_2.setSound('C', secs=4, hamming=True)
    sound_2.setVolume(1, log=False)
    sound_3.setSound('D', secs=4, hamming=True)
    sound_3.setVolume(1, log=False)
    # keep track of which components have finished
    trialComponents = [movie, sound_1, noise, sound_2, noise_2, sound_3, noise_3]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    #generar randoms para tiempos de sonido e imágenes
    texe=rdm.sample(range(600,1245,1),3)
    
    t1=texe[0]
    t2=texe[1]
    t3=texe[2]
    n=1
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie* updates
        if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            movie.frameNStart = frameN  # exact frame index
            movie.tStart = t  # local t and not account for scr refresh
            movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
            movie.setAutoDraw(True)
        if movie.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > movie.tStartRefresh + 1290-frameTolerance:
                # keep track of stop time/frame for later
                movie.tStop = t  # not accounting for scr refresh
                movie.frameNStop = frameN  # exact frame index
                win.timeOnFlip(movie, 'tStopRefresh')  # time at next scr refresh
                movie.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= t1-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # *noise* updates
        if noise.status == NOT_STARTED and tThisFlip >= t1-frameTolerance:
            # keep track of start time/frame for later
            noise.frameNStart = frameN  # exact frame index
            noise.tStart = t  # local t and not account for scr refresh
            noise.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
            noise.setAutoDraw(True)
        if noise.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                noise.tStop = t  # not accounting for scr refresh
                noise.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noise, 'tStopRefresh')  # time at next scr refresh
                noise.setAutoDraw(False)
        if noise.status == STARTED:
            if noise._needBuild:
                noise.buildNoise()
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= t2-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        
        # *noise_2* updates
        if noise_2.status == NOT_STARTED and tThisFlip >= t2-frameTolerance:
            # keep track of start time/frame for later
            noise_2.frameNStart = frameN  # exact frame index
            noise_2.tStart = t  # local t and not account for scr refresh
            noise_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_2, 'tStartRefresh')  # time at next scr refresh
            noise_2.setAutoDraw(True)
        if noise_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                noise_2.tStop = t  # not accounting for scr refresh
                noise_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noise_2, 'tStopRefresh')  # time at next scr refresh
                noise_2.setAutoDraw(False)
        if noise_2.status == STARTED:
            if noise_2._needBuild:
                noise_2.buildNoise()
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and tThisFlip >= t3-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3.play(when=win)  # sync with win flip
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
                sound_3.stop()
        
        # *noise_3* updates
        if noise_3.status == NOT_STARTED and tThisFlip >= t3-frameTolerance:
            # keep track of start time/frame for later
            noise_3.frameNStart = frameN  # exact frame index
            noise_3.tStart = t  # local t and not account for scr refresh
            noise_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_3, 'tStartRefresh')  # time at next scr refresh
            noise_3.setAutoDraw(True)
        if noise_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                noise_3.tStop = t  # not accounting for scr refresh
                noise_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noise_3, 'tStopRefresh')  # time at next scr refresh
                noise_3.setAutoDraw(False)
        if noise_3.status == STARTED:
            if noise_3._needBuild:
                noise_3.buildNoise()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            # Example script
            'reciever = DataReceiver()'
            'session_length = 1000'
            'reciever.capture_start(session_length)'
            'reciever.add_capture()'
            'reciever.save_capture()'
            #'reciever.plot_session(''test_plot', 'show=True)''

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('movie.started', movie.tStartRefresh)
    trials.addData('movie.stopped', movie.tStopRefresh)
    sound_1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_1.started', sound_1.tStartRefresh)
    trials.addData('sound_1.stopped', sound_1.tStopRefresh)
    trials.addData('noise.started', noise.tStartRefresh)
    trials.addData('noise.stopped', noise.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    trials.addData('noise_2.started', noise_2.tStartRefresh)
    trials.addData('noise_2.stopped', noise_2.tStopRefresh)
    sound_3.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_3.started', sound_3.tStartRefresh)
    trials.addData('sound_3.stopped', sound_3.tStopRefresh)
    trials.addData('noise_3.started', noise_3.tStartRefresh)
    trials.addData('noise_3.stopped', noise_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'
#voltage = list(map(lambda dp: dp.voltage, session_data.values()))
#temp = list(map(lambda dp: dp.temperature, session_data.values()))
print('t1=',t1)
print('t2=',t2)
print('t3=',t3)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
