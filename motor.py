import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
import pybullet as p

class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude=c.amplitudeF
        self.frequency=c.frequencyF
        self.offset=c.phaseOffsetF
        if self.jointName=="Torso_BackLeg":
            self.frequency=self.frequency/2.0
        self.values=self.amplitude*np.sin(self.frequency*np.arange(0,2*np.pi,2*np.pi/c.num_iterations)+self.offset)

    def Set_Value(self,robotId,t):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, 
                                    jointName=self.jointName, 
                                    controlMode=p.POSITION_CONTROL, 
                                    targetPosition=self.values[t], 
                                    maxForce=c.maxForce)

    def Save_Values(self):
        np.save("data/"+self.jointName+"MotorValues",self.values)