from distance import *
from distanceRight import *
from DBConnector import *

while True:
    if SensorRangeRight() < 60:
        if SensorRangeLeft() < 60:
            print ("1")
            #insert1()
    elif SensorRangeLeft() < 60:
        if SensorRangeRight() < 60:
            print("2")
            #insert2()
