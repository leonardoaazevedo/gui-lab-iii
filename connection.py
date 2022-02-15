import sys
from PIL import Image
import numpy as np
import time
import math
import array

from PyQt5 import QtGui
try:
    import sim
except:
    print ('Error import sim. Verify files and settings Coppelia.')

def radian2degree(angle):
    return 180*angle/math.pi

def degree2radian(angle):
    return math.pi*angle/180

def scale_img(im, nR, nC):
    nR0 = len(im)     # source number of rows
    nC0 = len(im[0])  # source number of columns
    return [[ im[int(nR0 * r / nR)][int(nC0 * c / nC)]
                for c in range(nC)] for r in range(nR)]


class Connection(object):
    def __init__(self, radius=7.5, showIm=False):
        self.showImage = showIm
        self.magnetStatus = False
        self.craneStatus = False
        self.connectionStatus = False
        self.distanceClaw = 2*math.pi*radius #0 a 360 verificar tamanho total e fazer a conta de comprimento 2*pi*r pra direita aumenta x. Pra esquerda diminui x se chegar ao total volta a 0 se for negativo vai pra 360
        self.currentDistanceClaw = 0
        self.currentAngleClaw = 0
        self.currentHeightHook = 0

    def init_connection(self, ip='127.0.0.1', port=19997):
        # print ('Program started')
        sim.simxFinish(-1)  # just in case, close all opened connections
        clientID = sim.simxStart(ip, port, True, True, 5000, 5)  # Connect to CoppeliaSim
        if clientID == -1:
            return -1, False
        self.clientID = clientID
        self.connectionStatus = True

        # Get Coppelia Objects ID
        self.boom = sim.simxGetObjectHandle(clientID, 'Atuador_braco', sim.simx_opmode_blocking)[-1]
        self.claw = sim.simxGetObjectHandle(clientID, 'Atuador_garra', sim.simx_opmode_blocking)[-1]
        self.crane = sim.simxGetObjectHandle(clientID, 'Atuador_guindaste', sim.simx_opmode_blocking)[-1]
        self.magnet = sim.simxGetObjectHandle(clientID, 'suctionPad', sim.simx_opmode_blocking)[-1]
        self.cam = sim.simxGetObjectHandle(clientID, 'Vision_sensor', sim.simx_opmode_blocking)[-1]
        self.cam2 = sim.simxGetObjectHandle(clientID, 'cam2', sim.simx_opmode_blocking)[-1]
        self.proximity_sensor = sim.simxGetObjectHandle(clientID, 'Proximity_sensor', sim.simx_opmode_blocking)[-1]
        self.boomStructure = sim.simxGetObjectHandle(clientID, 'Braco', sim.simx_opmode_blocking)[-1]

        self.err_code, _, _ = sim.simxGetVisionSensorImage(clientID, self.cam, 0, sim.simx_opmode_streaming)
        self.err_code, _, _ = sim.simxGetVisionSensorImage(clientID, self.cam2, 0, sim.simx_opmode_streaming)
        self.status = sim.simxReadProximitySensor(clientID, self.proximity_sensor, sim.simx_opmode_streaming)[1]

        return self.clientID, self.connectionStatus

    def closeConnection(self):
        # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
        sim.simxGetPingTime(self.clientID)
        # Now close the connection to CoppeliaSim:
        sim.simxFinish(self.clientID)

    # "Liga" guindaste
    def commandCraneOnOff(self):
        if self.connectionStatus:
            if self.craneStatus:
                sim.simxStopSimulation(self.clientID, sim.simx_opmode_blocking)
            else:
                # Inicia simulacao
                sim.simxStartSimulation(self.clientID, sim.simx_opmode_blocking)
                sim.simxSetJointTargetPosition(self.clientID, self.boom, 0, sim.simx_opmode_continuous)
                sim.simxSetJointTargetPosition(self.clientID, self.crane, 0, sim.simx_opmode_continuous)
            self.craneStatus = not self.craneStatus
        return self.craneStatus

    def getCraneStatus(self):
        return self.craneStatus