from distance import *
from distanceRight import *


left = distanceLeftC
right = distanceRightC


while True:
    SensorRangeLeft()
    SensorRangeRight()

    if left < 50:
        print ("1")
    if right < 50:
        print ("2")