import sys

if len(sys.argv)!= 1:
 distance = sys.argv[1]
 time = sys.argv[2]
 print("User provided values:")
else:
 print("No input values - using deafault values")
 distance = 100
 time = 50
 
 speed = distance/time

 print("--Speed Details")
 print("Distance", distance)
 print("Time", time)
 print("Speed", speed)
 print("-------")

