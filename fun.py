##next--clean up code and annotate

#codes the functions necessary to run 'runProject.py'
#define main monitor screen as 'testMonitor'

from psychopy import visual, event, core, misc
from psychopy.hardware import keyboard

import numpy
import random


#define global variables
win=None
fix=None
rect=None

kb=None
mouse=None
log_file=None

three=None
six=None
twelve=None

color_dir=None
color_wheel=None
color_select=None

rating_dir1=None
rating_dir2=None
myRatingScale=None

d1=None
d2=None
p1=None
p2=None
p3=None
p4=None
p5=None
p6=None
p7=None



#Input: None
#Output:None
#Initialize project intro and practice trial instructions
def InitializeDirections():
    global d1, d2
    global p1, p2, p3, p4, p5, p6, p7

    #d1 and d2: Introduce the Experiment
    d1=visual.TextStim(
        win, 
        height=1.5,
        wrapWidth=30,
        color='blue',
        pos=(-1.5,9),
        text='''
        Welcome to Kelle's coding project!
        ''')
    
    d2=visual.TextStim(
        win, 
        height=0.6,
        wrapWidth=28,
        color='black',
        pos=(-0.7,1),
        text='''
        In this task, we will see how well you can time three different intervals. 
        Without actively counting, you must wait and press any key when you 
        feel the interval has elapsed.\n\n
        But that's not all. Some trials will have a background constantly changing 
        colors. At the end of those trials, you will have to report the color of the 
        screen at the end of the interval.\n\n\n\n
        Ready to start? Just kidding, let's do a practice trial. 
        Press any key to continue.
        ''')

    #p1-p8: Practice Trial Instructions
    p1=visual.TextStim(
        win,
        height=0.6,
        wrapWidth=28,
        color='black',
        pos=(-1,3),
        text='''
        At the beginning of each trial, a number will be displayed in the center of the screen. 
        This is the interval (in seconds) you will time. During the actual task, this number will 
        appear and disappear on its own.\n
        For this practice trial, press any key to display the interval.
        ''')

    p2=visual.TextStim(
        win,
        height=0.6,
        wrapWidth=28,
        color='black',
        pos=(-1,8),
        text='''
        The interval is 6 seconds but don't start timing until you see a small black square in the center 
        of the screen. During the task, this square will appear and disappear automatically. 
        For now, press any key to continue.
        ''')

    p3=visual.TextStim(
        win,
        height=0.6,
        wrapWidth=28,
        color='black',
        pos=(-1,8),
        text='''
          When you perceive 6 seconds have passed, press any key.
        ''')

    p4=visual.TextStim(
        win,
        height=0.6,
        wrapWidth=28,
        color='black',
        pos=(-1,8),
        text='''
        Here is the interval. This time, we'll wait for it to disappear on its own. Remember to start 
        timing when you see the black square and press any key at the end of the interval.
        ''')

    p5=visual.TextStim(
        win,
        height=0.6,
        wrapWidth=28,
        color='black',
        pos=(-1,8),
        text='''
          **Remember the screen color at the time you press**
        ''')

    p6=visual.TextStim(
        win,
        height=0.6,
        wrapWidth=28,
        color='black',
        pos=(-1,8),
        text='''
        Cool! Using the mouse, select the color of the background at the end of the interval.
        ''')

    p7=visual.TextStim(
        win,
        height=0.6,
        wrapWidth=28,
        color='black',
        pos=(-1,4),
        text='''
        Each trial will be like one of the two we just practiced: white or rainbow. For all trials, start 
        timing when you see the black square and press any key when the time has elapsed.
        There are 24 trials and three possible intervals lengths:  3, 6 or 12 seconds.\n\n
        When you are ready to start, press any key and the task will begin!
        ''')




#Input: None
#Output:None
#Make color wheel and color wheel directions
def MakeColorWheel():
    global color_wheel, color_select, color_dir
    
    #Color wheel directions
    color_dir=visual.TextStim(
        win,
        height=0.7,
        wrapWidth=28,
        color='black',
        pos=(-1,8),
        text='''
        Use the mouse to select the color of the screen at the end of the interval.
        ''')
    
    #Create array of colors in hsv
    hsv=numpy.ones([256,256,3], dtype=float)

    hsv[:,:,0]=numpy.linspace(0,360,256, endpoint=False)
    hsv[:,:,1]=1
    hsv[:,:,2]=1
    
    #Create color wheel
    color_wheel=visual.RadialStim(
        win, 
        tex=misc.hsv2rgb(hsv),
        angularCycles=1,
        interpolate=True,
        texRes=360,
        size=(10,10),
        pos=(-8,0))
    
    #Create color selection box
    color_select=visual.Rect(
        win,
        width=10,
        height=10,
        pos=(5,0),
        lineColor='black',
        fillColor='white')




#Input: None
#Output:None
#Draw rating scale and rating scale directions
def MakeRatingScale():
    global myRatingScale, rating_dir1, rating_dir2
    
    #Rating directions (rating_dir1 for practice trials, rating_dir2 for task)
    rating_dir1=visual.TextStim(
        win,
        height=0.6,
        wrapWidth=28,
        color='black',
        pos=(-1,3),
        text='''
        On the next screen you will use the keyboard arrows to select how well you timed the interval. 
        Select   "Early"   if you think you pressed well before the interval elapsed,   "Close"   if you think 
        you pressed approximately when the interval elapsed, or   "Late"   if you think you pressed well 
        after the interval elapsed. There's no right or wrong answer for this, just your own opinion! 
        (You will be asked to do this after each trial).\n\n
        Press any key to display the rating scale and make your selection.
        ''')

    rating_dir2=visual.TextStim(
        win,
        height=0.7,
        wrapWidth=28,
        color='black',
        pos=(-1,7),
        text='''
          Use the arrows to select how well you timed the interval.\n\n
                                   Press enter when done.''')
    
    #Initialize rating scale
    myRatingScale=visual.RatingScale(
        win,
        pos=(0,0),
        lineColor='black',
        markerStart='Close',
        choices=['Early', 'Close', 'Late'])




#Input: None
#Output:None
#Make all other visual stims
def MakeVisualStim():
    global rect, fix
    global three, six, twelve

    three=visual.TextStim(
        win, 
        height=3, 
        color='black', 
        pos=(0,0), 
        text="3")
    
    six = visual.TextStim(
        win, 
        height=3, 
        color='black', 
        pos=(0,0), 
        text="6")

    twelve=visual.TextStim(
        win, 
        height=3, 
        color='black', 
        pos=(0,0), 
        text="12")

    rect=visual.Rect(
        win, 
        width=200, 
        height=100, 
        fillColorSpace='hsv', 
        fillColor=[0,0,1])

    fix=visual.GratingStim(
        win, 
        size=0.5, 
        pos=[0,0], 
        sf=0, 
        color='black')




#input: None
#ouput: None
#Load everything and open data file
##Update monitor name and new subject file name
def Initialize():
    global win
    global kb, mouse
    global log_file

    ##Change data file for each new subject (sub_01.csv, sub_02.csv, etc.)
    log_file=open('C:/Users/Kelle/Desktop/Python/scripts/python scripts/sub_06.csv', 'a')
    
    #Initialize window
    ##Define main monitor as 'testMonitor' OR update below
    win = visual.Window(
        [1024,768], 
        monitor='testMonitor', 
        units='deg', 
        color='white', 
        fullscr=True)

    #initialize directions, color wheel, rating scale and all other visual stim
    InitializeDirections()
    MakeColorWheel()
    MakeRatingScale()
    MakeVisualStim()
    
    #initialize mouse and keyboard
    mouse=event.Mouse()
    kb=keyboard.Keyboard()




#Input: None
#Output:None
#Introduces the task and walks participant through 2 example trials 
def ShowInstructions():
    global win
    global d1, d2, d3
    global p1, p2, p3, p4, p5, p6, p7, p8
    global six, twelve
    global myRatingScale, rating_dir1, rating_dir2
    global log_file
    
    #Introduce task, press any key to advance
    while not event.getKeys():
        d1.draw()
        d2.draw()
        win.flip()
    
    ##First Practice Trial ('White' trial)
    #Explain interval number display, press any key to advance
    while not event.getKeys():
        p1.draw()
        win.flip()
    
    core.wait(0.5)
    six.draw()
    win.flip()
    core.wait(0.5)
    
    #Display practice interval "6"
    while not event.getKeys():
        six.draw()
        p2.draw()
        win.flip()
    
    win.flip()
    core.wait(1)
        
    #Show fixation box and explain, press any key to advance
    while not event.getKeys():
        fix.draw()
        p3.draw()
        win.flip()
        
    #Show scale and explain, press ENTER to advance
    event.clearEvents()
    
    while not event.getKeys():
        rating_dir1.draw()
        win.flip()
    
    RatingScale()
    
    ##Second Practice Trial ('Rainbow' trial)
    #Display practice interval '12', will advance automatically
    p4.draw()
    twelve.draw()
    win.flip()
    core.wait(10)
    win.flip()
    core.wait(2)
    
    #Reset keyboard responses
    event.clearEvents(eventType='keyboard')
    
    #Show fixation square with color changing background, press any key to advance
    color=1
    while not event.getKeys():
        if color==-1:
            fix.draw()
            win.flip()
        else:
            rect.setFillColor([color,1,1])
            rect.draw()
            fix.draw()
            p5.draw()
            win.flip()
            core.wait(0.05)
            color+=2
    
    p6.draw()
    win.flip()
    
    ColorSelect()
    RatingScale()
    
    #Final directions before task begins
    while not event.getKeys():
        p7.draw()
        win.flip()
    
    win.flip()
    core.wait(5)




#Input: background start color: hsv[0]
#Output:selected color [hsv]
#Use mouse to click color from color wheel, display color in box to the right
def ColorSelect(color=0):
    global win, rect, fix
    global mouse, kb
    global color_select, color_dir
    
    mouse_click=True
    
    #if its a 'white' trial, assign new color as -1 and continue without color selection
    if color==-1:
        new_color=[-1,1,1]
    else:
        mouse_click=False
    
    #until the mouse is clicked, update mouse position and display color mouse is on
    while mouse_click==False:
        mouse_pos=mouse.getPos()    #find mouse position
        dx=mouse_pos[0]+8           #assign x value, +8 to adjust for wheel location
        dy=mouse_pos[1]             #assign y value
            
        #get circle radius (distance from mouse to color wheel center)
        r=numpy.sqrt((dx**2)+(dy**2))
        
        #if mouse is in the center of the circle, make radius 1
        if r<0.0001:
            r=1
            
        #find the degree that corresponds to the mouse location
        hue=numpy.arccos(dy/r)/(numpy.pi/180)
        
        #adjust x value to be positive
        if dx<0:
            hue=360-hue
        
        #assign value to color mouse is over
        new_color=[hue,1,1]
        
        #if mouse is outside the color wheel, display white
        if r>5:
            new_color=[0,0,1]
        
        #fill display with color mouse is over
        color_select.setFillColor(new_color, 'hsv')
        
        #display colorwheel, display, and directions
        color_wheel.draw()
        color_select.draw()
        color_dir.draw()
        win.flip()
        
        #don't allow mouse clicks outside of color wheel
        if r<5:
            buttons=mouse.getPressed()
            mouse_click=buttons[0]

    return(new_color)




#Input: None
#Output:selected rating, string-'Early', 'Close', or 'Late'
#Display rating scale and directions, press ENTER to select
def RatingScale():
    global win
    global kb
    global myRatingScale, rating_dir2

    myRatingScale.noResponse=True
    
    #show and update rating scale until ENTER is pressed
    while myRatingScale.noResponse:
        myRatingScale.draw()
        rating_dir2.draw()
        win.flip()
    
    #get selected rating for the output
    rating=myRatingScale.getRating()
    
    return(rating)




#Input: None
#Output: 24 combos of [0] start color and [1] interval 
#Should have 8 trials of each interval
#Each item in output list is 1 trial 
def GenerateTrialSequence():

    trials=[]
    
    #start color options: 4 'rainbow' trials, 4 'white' trials (-1)
    colors=[0, 120, 180, 300, 
            -1, -1, -1, -1]
    
    #three interval options (in seconds)
    intervals=[3,6,12]
    
    #make all combinations of start colors and trial intervals
    for int in intervals:
        for col in colors:
            t =[col,int]
            trials.append(t)
    
    #return list of trials
    return trials




#Input: Trial sequence list
#Output:None
#Randomizes order of trial sequence list
def RandomizeTrialSequence(trials):
    random.shuffle(trials)




#Input: Randomized trial sequence list: [color[0], interval]...
#Output:Responses for each trial [timed color, ]
#If color==-1, it is a colorless/'white' trial
def RunTrial(color=0, interval=30):
    global win, rect, fix
    global kb
    global myRatingScale, rating_dir2
    global log_file

    response=''
    
    color_start=color
    #Add trial info to response line
    response+='trial_interval, ' + str(interval) + ', ' + 'trial_color, ' + str(color_start) + ', '
    
    #Display interval for this trial
    if interval==3:
        three.draw()
        win.flip()
        core.wait(2)
    elif interval==6:
        six.draw()
        win.flip()
        core.wait(2)
    elif interval==12:
        twelve.draw()
        win.flip()
        core.wait(2)
    
    win.flip()
    core.wait(1)
    
    
    #reset keyboard responses
    kb.clock.reset()
    kb.clearEvents()
    event.clearEvents(eventType='keyboard')
    
    rainbow=color
    #Until key has been pressed, flip fixation square
    #If a 'rainbow' trial, also change background color, starting on trial "color"
    while not event.getKeys():
        if rainbow==-1:
            fix.draw()
            win.flip()
        else:
            rect.setFillColor([rainbow,1,1])
            rect.draw()
            fix.draw()
            win.flip()
            core.wait(0.05)
            rainbow+=2
    
    win.flip()
    core.wait(0.5)
    
    #If color!=0 (i.e. Rainbow trial), display color wheel and have participant select a color
    color_selected=ColorSelect(color)
    
    #If a key press has been made, find RT for key press and add to responses
    ptbKeys=kb.getKeys()
    if ptbKeys!=[]:
        response+='RT, ' + f"{ptbKeys[0].rt:.4f}" + ", "
    else:
        response+='-1' + ", "
    
    #Add color at key press (timed color) and chosen color from color wheel
    response+='color_end, ' + str(rainbow) + ', selected_color, ' + f"{color_selected[0]:.4f}" + ', '
    
    win.flip()
    core.wait(1)

    #Display rating scale, ENTER to advance
    rating=RatingScale()

    #Add rating selection to responses
    response+=rating
    
    #Add all responses to log file, move to next row
    log_file.write(response + "\n")
    
    ##Can remove this when log_file is good to go
    return(response)




#Input: List of trials from generating sequence
#Output:None
#For each item in trial list, run task
def RunTask(trials):


    for i in range(len(trials)):
        RunTrial(trials[i][0], trials[i][1])





#Input: None
#Output:None
#Closes log_file, closes window and quits core
def TerminateTask():
    global win
    global log_file

    log_file.close()
    win.close()
    core.quit()
