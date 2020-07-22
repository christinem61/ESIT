from gpiozero import Button
import RPi.GPIO as IO
import time
from signal import pause
import os
#from Naked.toolshed.shell import execute_js, muterun_js

IO.cleanup()
IO.setwarnings(False)       #do not show any warnings
IO.setmode(IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN39 as 'GPIO19')
IO.setup(19,IO.OUT)         # initialize GPIO19 as an output.
IO.setup(21,IO.IN)               #initialize GPIO26 as input
button = Button(21)


IO.output(19, True)
button.wait_for_press(timeout=None)
IO.output(19, False)
















