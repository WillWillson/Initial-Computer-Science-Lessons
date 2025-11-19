###########################################################################################
# Name: William Wilson
# Date: 10/11/2020
# Description: It asks for the name and age, and the doubles the age.
###########################################################################################

# function that prompts the user for a name and returns it

def name():
    name = str(input("Please enter your name: "))
    return name

# function that receives the user's name as a parameter, and prompts the user for an age and returns it

def age (name):
    age = int(input("How old are you, " + name + "? "))
    return  age

# function that receives the user's name and age as parameters and displays the final output

def output (name, age):
    print("Hi, " + name + ". You are " + str(age) + " years old. Twice your age is " + str((age * 2)) + ".")
     

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get the user's name

name = name()

# get the user's age

age = age (name)

# display the final output

output = output (name, age)
