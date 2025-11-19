###########################################################################################
# Name: William Wilson
# Date: 11/6/20
# Description: 
###########################################################################################

# function that:
# (1) prompts the user for a list size

def size():
    size1 = input("How many integers would you like to add to the list? ")
    return int(size1)

# (2) prompts the user for the integers to store in the list (corresponding to the list size)

def numbers():
    counter = 0
    numList = []
    while counter < size1:
       number = int(input("Enter an integer: "))
       numList.append(number)
       counter += 1
    return numList

# (3) creates the list

def list1():
    numList = numbers()
    return numList

# (4) returns the list

def returnList():
    print("The original list: " + str(numList))

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list

size1 = size()
numList = list1()
returnList()

# display information about the list using the list functions discussed in class
# there is no need to write/call your own functions here

print("The length of the list is " + str(len(numList)) + ".")
print("The minimum value in the list is " + str(min(numList)) + ".")
print("The maximum value in the list is " + str(max(numList)) + ".")
numList.reverse()
print("The reversed list: " + str(numList))
numList.sort()
print("The sorted list: " + str(numList))
