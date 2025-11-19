###########################################################################################
# Name: WIlliam Wilson
# Date: 10/12/20
# Description: 
###########################################################################################

# function that prompts the user to enter an integer and returns it

def number ():
    number = int(input("Enter an integer: "))
    if number != int:
        print("String")
        
    return number

# function that receives three integers as parameters and returns the minimum of the three

def minimum(a, b, c):
    if b >= a and c >= a:
        return a
    if a >= b and c >= b:
        return b
    if a >= c and b >= c:
        return c

# function that receives three integers as parameters and returns the maximum of the three

def maximum (a, b, c):
    if b <= a and c <= a:
        return a
    if a <= b and c <= b:
        return b
    if a <= c and b <= c:
        return c

# function that receives three integers as parameters, and calculates and returns the mean

def mean (a, b, c):
    return ((a + b + c)/3)
    
    
# function that receives three integers as parameters, and calculates and returns the median

def median (a, b, c):
    if a >= b and a <= c or a <= b and a >= c:
        return a
    if b >= a and b <= c or b <= a and b >= c:
        return b
    if c >= a  and c <= b or c <= a and c >= b:
        return c
    if a == b == c:
        return a
    
# function that receives three integers as parameters, and calculates and returns the mode

def mode (a, b, c):
    if a == b or a == c:
        return a
    if b == a or a == c:
        return b
    if c == a or c == b:
        return c
    else:
        return "undefined"
   
# function that receives three integers as parameters, and calculates and returns the range

def theRange(a, b, c):
    if b <= a and c <= a and b >= a and c >= a:
        return (a - a)
    if b <= a and c <= a and a >= b and c >= b:
        return (a - b)
    if b <= a and c <= a and a >= c and b >= c:
        return (a - c)
    if a <= b and c <= b and a >= b and c >= b:
        return (b - b)
    if a <= b and c <= b and b >= a and c >= a:
        return (b - a)
    if a <= b and c <= b and a >= c and b >= c:
        return (b - c)
    if a <= c and b <= c and a >= c and b >= c:
        return (c - c)
    if a <= c and b <= c and b >= a and c >= a:
        return (c - a)
    if a <= c and b <= c and a >= b and c >= b:
        return (c - b)

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get three integers from the user
a = number()
b = number()
c = number()

# determine and display the minimum value

minimum = print("The minimum value is " + str(minimum(a, b, c)) + ".")

# determine and display the maximum value

maximum = print("The maximum value is " + str(maximum(a, b, c)) + ".")

# calculate and display the mean

mean = print("The mean is " + str(mean(a, b, c)) + ".")

# calculate and display the median

median = print("The median is " + str(median(a, b, c)) + ".")

# calculate and display the mode

mode = print("The mode is " + str(mode(a, b, c)) + ".")

# calculate and display the range

theRange = print("The range is " + str(theRange(a, b, c)) + ".")
