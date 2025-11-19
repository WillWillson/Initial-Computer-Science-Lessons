###########################################################################################
# Name: William Wilson
# Date: 11/12/2020
# Description: This code generates a random list of integers, such that both its length and its minimum and maximum values added to the list provided by the user.
###########################################################################################

from random import randint

# function that prompts the user for a list size, minimum and maximum values, creates the list, and returns it
# you must use the list functions discussed in class to add integers to the list

def listSize():
    size1 = int(input("How many random integers would you like to add to the list? "))
    minimum1 = int(input("What would you like the minimum value to be? "))
    maximum1 = int(input("What would you like the maximum value to be? "))

    for i in range(size1):
        num = randint(minimum1, maximum1)
        numbers.append(num)
    print("The list: {}" .format(numbers))
    return size1
        


# function that receives the list as a parameter, and calculates and returns the mean

def mean(numbers):
    index = 0
    for n in numbers:
        index += n
    mean1 = (index/size1)
    print("The mean of the list is {}." .format(mean1))
  
# function that receives the list as a parameter, and calculates and returns the median

def median(numbers):
    numbers.sort()
    n = len(numbers)
    first = 0
    last = n - 1
    if size1 % 2 == 0:
        mid = (first + last) // 2
        median1 = (numbers[mid] + numbers[mid + 1]) / 2
    else:
        mid = (first + last) // 2
        median1 = numbers[mid]
    print("The median of the list is {}".format(median1))
    return median1
    

# function that receives the list as a parameter, and calculates and returns the range

def listRange(numbers):
    numbers.sort()
    n = len(numbers)
    first = 0
    last = n - 1
    range1 = numbers[last] - numbers[first]
    print("The range of the list is {}.".format(range1))
    return range1


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list

numbers = []

# display the list
# there is no need to write/call your own function for this part

size1 = listSize()

# calculate and display the mean

mean1 = mean(numbers)

# calculate and display the median

median1 = median(numbers)

# calculate and display the range

range1 = listRange(numbers)
