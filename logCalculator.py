# Created by: James Lee
# Created on: Feb 2019
# Created for: ICS4U
# This program calculates the amount of logs that can fit on a truck given its length

# State variables
numberOfLogs = 0
logLength = 0
singleLogWeight = 0
truckTotalCapacity = 1100
logWeight = 20

# Find log length from user
logLength = input("What is the log length in metres? Can be either 0.25, 0.5, or 1 : ")

# Find weight of a single log specified by user
singleLogWeight = logLength * logWeight

# Find total number of logs that can fit in truck
numberOfLogs = truckTotalCapacity/singleLogWeight

# Shows result
print("The truck can carry " + str(numberOfLogs) + " logs of " + str(logLength) + " metres.")
