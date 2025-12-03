import sys

# If user provides exactly 2 values
if len(sys.argv) == 3:
    distance = float(sys.argv[1])
    time = float(sys.argv[2])
    print("User provided values:")
else:
    print("No input values - using default values")
    distance = 100
    time = 50

speed = distance / time

print("----- Speed Details -----")
print("Distance:", distance)
print("Time:", time)
print("Speed:", speed)
print("-------------------------")
