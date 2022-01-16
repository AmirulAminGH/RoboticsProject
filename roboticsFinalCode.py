from robolink import *
from robodk import *
import json
RDK = Robolink()
robot = RDK.Item('', ITEM_TYPE_ROBOT)

scale = mbox('Enter the scale down value', entry=True)
scale = float(scale)
breakThreshold = mbox('Enter break away threshold value',entry=True)
breakThreshold= float(breakThreshold) 

target= RDK.Item('Target 1')
home= RDK.Item('Home')

target_pose=target.Pose()

startPoint= target_pose.Pos()
robot.MoveJ(target)
with open('E:/Documents/Assignment Sem 1 4th Year/Robotics mini project/nameCoords.json') as data_file:
  dataCoords=json.load(data_file)
arrayNum = len(dataCoords)-1
for i in range(arrayNum):

  x= startPoint[0]+(dataCoords[i][0]/scale)
  y=startPoint[1]+(dataCoords[i][1]/scale)
  z= startPoint[2]-200

  breakPointX1=startPoint[0]+(dataCoords[i][0]/scale)
  breakPointX2=startPoint[0]+(dataCoords[i+1][0]/scale)

  breakPointY1=startPoint[1]+(dataCoords[i][1]/scale)
  breakPointY2=startPoint[1]+(dataCoords[i+1][1]/scale)

  breakDeltaX=breakPointX1-breakPointX2
  breakDeltaX = abs(breakDeltaX)

  breakDeltaY=breakPointY1-breakPointY2
  breakDeltaY = abs(breakDeltaY)

  if breakDeltaX > breakThreshold:
    z= startPoint[2]
  
  if breakDeltaY > breakThreshold:
    z= startPoint[2]
  

  target_pose.setPos([x,y,z])
  robot.MoveL(target_pose)
robot.MoveJ(target)
robot.RunInstruction('Program_Done')