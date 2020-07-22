#SERVER SIDE (PYTHON)
# for pi2 = connected to monitor
# add sorting of train cars? sounds kind of difficult but would be nice

import socket
import time

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

(CONNECTION, ADDRESS) = s.accept()
print(ADDRESS)
print('connection found...')

    
data = CONNECTION.recv(1024).decode("utf-8")
msg = data
data = int(data)

if data <= 100:
    print(data)
CONNECTION.close()