# Make sure to have the server side running in CoppeliaSim: 
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
import sys
import numpy as np
from readchar import readchar

import matplotlib.pyplot as mpl

try:
    import sim
except:
    print('--------------------------------------------------------------')
    print('"sim.py" could not be imported. This means very probably that')
    print('either "sim.py" or the remoteApi library could not be found.')
    print('Make sure both are in the same folder as this file,')
    print('or appropriately adjust the file "sim.py"')
    print('--------------------------------------------------------------')
    print('')

import time as time

# tecla = readchar()

def MovimentarGuindaste(clientID, eixoTraseiroEsquerdo, eixoTraseiroDireito, val):
    newVal = val * 0.1
    sim.simxSetJointTargetVelocity(clientID, eixoTraseiroEsquerdo, newVal, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, eixoTraseiroDireito, -newVal, sim.simx_opmode_oneshot)
    time.sleep(0.2)
    sim.simxSetJointTargetVelocity(clientID, eixoTraseiroEsquerdo, 0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, eixoTraseiroDireito, 0, sim.simx_opmode_oneshot)


print('Program started')
sim.simxFinish(-1)  # just in case, close all opened connections
clientID = sim.simxStart('127.0.0.1', 8080, True, True, 5000, 5)  # Connect to CoppeliaSim
if clientID != -1:
    print('Connected to remote API server')

    # Get Crane Handles
    eixoTraseiroEsquerdo = sim.simxGetObjectHandle(clientID, 'RodaEixo6', sim.simx_opmode_blocking)[-1]
    eixoTraseiroDireito = sim.simxGetObjectHandle(clientID, 'RodaEixo1', sim.simx_opmode_blocking)[-1]

    # Enable imshow
    mpl.ion()

    try:
        while (1):
            command = input('Command: ')

            # Move foward
            if command == 'w':
                MovimentarGuindaste(clientID, eixoTraseiroEsquerdo, eixoTraseiroDireito, 1)
            # Move back
            if command == 's':
                MovimentarGuindaste(clientID, eixoTraseiroEsquerdo, eixoTraseiroDireito, -1)


    except KeyboardInterrupt:
        sim.simxFinish(clientID)
        sys.exit()

else:
    print('Failed connecting to remote API server')
print('Program ended')
