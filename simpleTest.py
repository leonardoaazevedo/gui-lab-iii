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
import time as time


def levantarGuindaste(clientID, lancaVertical, pistao, expandir_pistao,  val):
    newVal = val * 0.1
    newValPistao = val * 0.05
    newValExpandirPistao = val * 1
    sim.simxSetJointTargetVelocity(clientID, lancaVertical, newVal, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, pistao, newValPistao, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, expandir_pistao, newValExpandirPistao, sim.simx_opmode_oneshot)
    time.sleep(0.2)
    sim.simxSetJointTargetVelocity(clientID, lancaVertical, 0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, pistao, 0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, expandir_pistao, 0, sim.simx_opmode_oneshot)


def rotacionar(clientID, cabine_rotacao , val):
    newVal = val * 10000000000
    sim.simxSetJointTargetVelocity(clientID, cabine_rotacao, newVal, sim.simx_opmode_oneshot)
    time.sleep(0.2)
    sim.simxSetJointTargetVelocity(clientID, cabine_rotacao, 0, sim.simx_opmode_oneshot)


def expandir_lanca(clientID, lanca1, lanca2, lanca3 , val):
    newVal = val * 0.1
    sim.simxSetJointTargetVelocity(clientID, lanca1, newVal, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, lanca2, newVal, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, lanca3, newVal, sim.simx_opmode_oneshot)
    time.sleep(0.2)
    sim.simxSetJointTargetVelocity(clientID, lanca1, 0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, lanca2, 0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, lanca3, 0, sim.simx_opmode_oneshot)



def mover_frente(clientID, roda_esquerda, roda_direita, val):
    newVal = val * 100
    sim.simxSetJointTargetVelocity(clientID, roda_esquerda, newVal, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, roda_direita, -newVal, sim.simx_opmode_oneshot)
    time.sleep(0.2)
    sim.simxSetJointTargetVelocity(clientID, roda_esquerda, 0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, roda_direita, 0, sim.simx_opmode_oneshot)

def mover_tras(clientID, roda_esquerda, roda_direita, val):
    newVal = -val * 100
    sim.simxSetJointTargetVelocity(clientID, roda_esquerda, newVal, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, roda_direita, -newVal, sim.simx_opmode_oneshot)
    time.sleep(0.2)
    sim.simxSetJointTargetVelocity(clientID, roda_esquerda, 0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, roda_direita, 0, sim.simx_opmode_oneshot)

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

print('Program started')
sim.simxFinish(-1)  # just in case, close all opened connections
clientID = sim.simxStart('25.54.18.181', 8080, True, True, 5000, 5)  # Connect to CoppeliaSim
if clientID != -1:
    print('Connected to remote API server')

    pistao = sim.simxGetObjectHandle(clientID, 'Pistao_joint0', sim.simx_opmode_blocking)[-1]
    lancaVerticalHandle = sim.simxGetObjectHandle(clientID, 'Lanca_joint0', sim.simx_opmode_blocking)[-1]
    roda_esquerda_handle = sim.simxGetObjectHandle(clientID, 'RodaEsquerda', sim.simx_opmode_blocking)[-1]
    roda_direita_handle = sim.simxGetObjectHandle(clientID, 'RodaDireita', sim.simx_opmode_blocking)[-1]
    expandir_pistao_handle = sim.simxGetObjectHandle(clientID, 'AmpliarPistaoi_joint0', sim.simx_opmode_blocking)[-1]
    cabine_rotacao_handle = sim.simxGetObjectHandle(clientID, 'Cabine_joint', sim.simx_opmode_blocking)[-1]
    lanca1 = sim.simxGetObjectHandle(clientID, 'Lanca1_joint', sim.simx_opmode_blocking)[-1]
    lanca2 = sim.simxGetObjectHandle(clientID, 'Lanca2_joint', sim.simx_opmode_blocking)[-1]
    lanca3 = sim.simxGetObjectHandle(clientID, 'Lanca3_joint', sim.simx_opmode_blocking)[-1]

    wheel_radius = 0.03
    max_speed = 3
    max_turn = 0.3
    speed = 0
    turn = 0
    b = 0.0565

    # Enable imshow
    mpl.ion()

    while 1:
        command = input('Command: ')

        if command == 'o':
            levantarGuindaste(clientID, pistao, lancaVerticalHandle, expandir_pistao_handle, 35)
        if command == 'l':
            levantarGuindaste(clientID, pistao, lancaVerticalHandle, expandir_pistao_handle, -35)
        if command == 'w':
            mover_frente(clientID, roda_esquerda_handle, roda_direita_handle, 100000)
        if command == 'a':
            rotacionar(clientID, cabine_rotacao_handle, 90000000)
        if command == 'd':
            rotacionar(clientID, cabine_rotacao_handle, -90000000)
        if command == 'e':
            expandir_lanca(clientID, lanca1, lanca2, lanca3, 30)
        if command == 'q':
            expandir_lanca(clientID, lanca1, lanca2, lanca3, -30)

else:
    print('Failed connecting to remote API server')
print('Program ended')





