# TESTS SYSTEM WITHOUT A BUTTON

import time
import socket
from signal import pause
import os
from Naked.toolshed.shell import execute_js, muterun_js


# Define host based on hostname -I (PI2 IP address)
# can't find IP address of other thing;
# find before demo, git push and git pull real quick
# run server on pi2

HOST = "192.168.43.158"     # Symbolic name meaning all available interfaces
PORT = 5007               # Arbitrary non-privileged port



# might want to change origin address
origin = '/home/pi/Desktop/pictures/origin.jpg'

def take_picture(pic):
    time.sleep(2)
    os.system("gpicview " + pic)

"""for i in range(3):
        take_picture('/home/pi/Desktop/pictures/'+ str(i) + '.jpg')"""

response = muterun_js('/home/pi/Desktop/ESIT/PI1/mismatch.js')

if response.exitcode == 0:
    print("sending")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    sock.connect(server_address)

    try:
        data = str(int(float((response.stdout)[0:-1])))
        sock.send(data.encode())
        print('Sending occupancy')
            # turn on LED?
    finally:
        sock.close()
