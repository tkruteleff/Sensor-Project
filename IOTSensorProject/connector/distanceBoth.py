from distance import *
from distanceRight import *


left = distanceLeftC
right = distanceRightC


while True:
    SensorRangeLeft()
    SensorRangeRight()

    if left > 50 & right > 50:
        print ("1")
