import pyrosim.pyrosim as pyrosim

length=1
width=1
height=1
x=0
y=0
z=.5

pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])

pyrosim.End()