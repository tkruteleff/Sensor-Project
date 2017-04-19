from distance import *
from distanceRight import *


while True:
    SensorRangeLeft()
    SensorRangeRight()

    if (SensorRangeLeft() > 50):
        print ("1")