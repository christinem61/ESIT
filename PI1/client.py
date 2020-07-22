import time
from gpiozero import Button
from picamera import PiCamera
import RPi.GPIO as IO
import socket
from signal import pause
from Naked.toolshed.shell import execute_js, muterun_js

IO.setwarnings(False)       # do not show any warnings
IO.setmode (IO.BCM)         # we are programming the GPIO by BCM pin numbers. (PIN39 as 'GPIO19')
IO.setup(19,IO.OUT)         # initialize GPIO19 as an output.
IO.setup(21,IO.IN)          # initialize GPIO26 as input
button = Button(21)

# Define host based on hostname -I (PI2 IP address)
# can't find IP address of other thing;
# find before demo, git push and git pull real quick
# run server on pi2

HOST = "192.168.43.158"     # Symbolic name meaning all available interfaces
PORT = 5007               # Arbitrary non-privileged port

camera = PiCamera()
camera.resolution = (1280,720)
IO.output(19,False)

# might want to change origin address
origin = '/home/pi/Desktop/pictures/origin.jpg'

def take_picture(pic):
    time.sleep(2)
    camera.capture(pic)

while 1:
    diff = 0
    button.wait_for_press()
    start_time = time.time()
    
    while button.is_active:
        now_time = time.time()
        diff = -start_time+now_time

    if diff >= 5 :           #long hold
        IO.output(19, True)
        time.sleep(.5)
        camera.capture(origin)
        IO.output(19, False)
        
    else:                   #short hold
        IO.output(19, True)
        time.sleep(5)

        for i in range(3):
            take_picture('/home/pi/Desktop/pictures/'+ str(i) + '.jpg')

        response = muterun_js('mismatch.js')

        if response.exitcode == 0:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (HOST, PORT)
            sock.connect(server_address)
            
            try:
                data = str(int(float((response.stdout)[0:-1])))
                sock.send(data.encode())
            finally:
                sock.close()
                IO.output(19, False)
