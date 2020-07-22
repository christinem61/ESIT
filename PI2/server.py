#SERVER SIDE (PYTHON)
# for pi2 = connected to monitor
# add sorting of train cars? sounds kind of difficult but would be nice

import socket
import time
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

import os

HOST = ''
PORT = 5007

#create a socket on the network using port 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#name of the host (router, unless it has no name, then return IP address)
HOSTNAME = socket.gethostname()
server_address = (HOST, PORT)
print('Hostname: %s' % HOSTNAME)
print(HOST)
print('starting up on %s port %s' % (server_address[0], server_address[1]))

#binds to the host and port
s.bind(server_address)
#listens to the bound host's port
#waits for (1) connection
s.listen(1)
print('listening for a connection...')

# graph code starts 
fig=plt.figure()

occupancy = [50,20,10]
x = range(1,4)
barcollection = plt.barh(x, occupancy)

# just graph setup
plt.xlim(0, 100)
plt.xlabel('Occupancy')
plt.ylabel('Car Number')
plt.title('Train Occupancy')
plt.yticks([1, 2, 3])
plt.xticks(np.arange(0, 101, 25))

#if a connection is found, accept it and create (object, string)


def animate(i):
    try:
        (CONNECTION, ADDRESS) = s.accept()
        print(ADDRESS)
        print('connection found...')
        
        #receive the data (up to 3 bytes or 24 bits or 2^24)
        
        data = CONNECTION.recv(1024).decode("utf-8")
        
        # checking data value
        # should send received if data = number?
        # data to int
        msg = data
        data = int(data)
        
        if data <= 100:
            #CONNECTION.send(msg.encode("utf-8"))
            y = [50, 20, data]
            for i, b in enumerate(barcollection):
                b.set_width(y[i])
            # graph code ends

        else:
            # how do you do this if you don't want the connection to close
            CONNECTION.close()

        CONNECTION.close()

    except KeyboardInterrupt:
       s.close()
       CONNECTION.close()

anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=500)
plt.show()
