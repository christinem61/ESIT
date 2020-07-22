from gpiozero import Button
import RPi.GPIO as IO
import time
from signal import pause
import os
from Naked.toolshed.shell import execute_js, muterun_js

IO.setwarnings(False)       #do not show any warnings
IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN39 as 'GPIO19')
IO.setup(19,IO.OUT)         # initialize GPIO19 as an output.
IO.setup(21,IO.IN)               #initialize GPIO26 as input
button = Button(21)

origin = '/home/pi/Desktop/pictures/origin.jpg'

def take_picture(pic):
    #camera.start_preview()
    os.system("gpicview " + pic)
    #camera.stop_preview()

while 1:
    diff = 0
    button.wait_for_press()
    start_time = time.time()
    
    while button.is_active:
        now_time = time.time()
        diff = -start_time+now_time

    if diff >= 5 :           #long hold
        IO.output(19, True)
        take_picture(origin)
        IO.output(19,False)
        
    else:                   #short hold
        response = muterun_js('/home/pi/Desktop/ESIT/PI1/mismatch.js')
        if response.exitcode == 0:
            print(response.stdout)

