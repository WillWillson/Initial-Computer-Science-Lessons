###########################################################################################
# Name: William WIlson
# Date: 10/4/20
# Description: This program should ask for the user name and age, and then double their age.
###########################################################################################

# prompt the user for a name and an age
name = input("Please enter your name: ")

age = input("How old are you, " + name + "? ")

# display the final output

print("Hi, {}. You are {} years old. Twice your age is {}." .format(name, age, int(age) * 2))
