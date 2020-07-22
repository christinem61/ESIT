from gpiozero import Button
from picamera import PiCamera
import RPi.GPIO as IO
import time
from signal import pause
import os
from Naked.toolshed.shell import execute_js, muterun_js

IO.setwarnings(False)       #do not show any warnings
IO.setmode(IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN39 as 'GPIO19')
IO.setup(19,IO.OUT)         # initialize GPIO19 as an output.
IO.setup(21,IO.IN)               #initialize GPIO26 as input
button = Button(21)

camera = PiCamera()
camera.resolution = (1280,720)

while 1:
    diff = 0
    button.wait_for_press()
    start_time = time.time()
    
    while button.is_active:
        now_time = time.time()
        diff = -start_time+now_time

    if diff >= 5 :           #long hold
        IO.output(19, True)
        camera.start_preview()
        button.wait_for_press(timeout=None)
        camera.capture("/home/pi/Desktop/test.jpg")
        camera.stop_preview()
        IO.output(19, False)
