##########################################################################################
# Name: William Wilson
# Date: 11/3/2020
# Description: This program will print out a table 
##########################################################################################

import math

# a function that displays the table
def table (min, max, interval):
    print("n\tSeq\tBin\tPerf")
    print("-------------------------------------------------------------------------------")
    for i in range(min, max+1,interval):
            sequential = SeqOf(i)
            binary = Binary(i)
            if binary == 0:
                perf = 0
            else:
                perf = (int(sequential / binary))
            print("{}\t{}\t{}\t{}".format(i, sequential, binary, perf))

# a function that calculates the average number of comparisons of a sequential search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def SeqOf(n):
    return(int(n/2))

# a function that calculates the maximum number of comparisons of a binary search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def Binary(n):
    if n == 0:
        return 0
    else:
        return(int(math.ceil(math.log(n,2))))

###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
min = -1
while(min < 0):
    min = int(input("Minimum number of list items (>=0)? "))
    if(min < 0):
        print("*ERROR: Minimum must be >= 0!")

# get user input for the maximum (make sure that is is >= minimum)
max = -1
while(max < min):
    max = int(input("Maximum number of list items (>= min (0))? "))
    if(max < min):
        print("*ERROR: Maximum must be >= minimum (100)!")

# get user input for the interval (make sure that it is >= 1)
interval = 0
while(interval < 1):
    interval = int(input("The interval between each row of the table(>= 1)? "))
    if(interval < 1):
        print("*ERROR: Interval must be >= 1!")

# generate the table
table(min, max, interval)
