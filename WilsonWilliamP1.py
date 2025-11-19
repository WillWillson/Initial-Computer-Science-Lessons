########################################################################################
# Name: William WIlson
# Date: 12/11/2020
# Description: Figure out how many zeros there are within a set of numbers.
########################################################################################

# Import time here
from time import time

# Call time
start_time = time()

# Main part of the code
def zeros(n):
    i = 1
    numZeros = 0
    while (i <= n):
        j = i
        while (j > 0):
            if (j % 10 == 0):
                numZeros += 1
            j = j // 10
        i += 1
    return numZeros

# Set up input
n = int(input("What number do you want to count zeros to? "))

# Start time
start = time()

# Print The results
result = zeros(n)

# End time
stop = time()

# Output of how many zeros there was
print("The number of zeros written from 1 to {} is {}.".format(n, result))

# The Time it took
print("This took {} seconds. ".format(stop - start))

