#############################################################
# Name: William Wilson
# Date: 2/4/21
# Description: This program will create a heads or tails game, and calculate the amount of wins each individual have.
#############################################################

# import things needed

import random

# function that creeats a random set of different solutions

def flip():
    result1 = int(2 * random.random()+1)
    return result1

# function that will run each game 

def gameNumPrint():
    for i in range(0, n):
        sums = []
        profWins = 0
        groupAWins = 0
        groupBWins = 0
        for l in range(0, k):
            first = flip()
            second = flip()
            sumOf = first + second
            sums.append(sumOf)
            if (first == 1 and second == 1):
                groupAWins += 1
            if (first == 2 and second == 2):
                groupBWins += 1
            if ((first == 1 and second == 2)or(first == 2 and second == 1)):
                profWins += 1
        c2 = sums.count(2)
        p2 = round((c2/len(sums))*100, 1)

        c3 = sums.count(3)
        p3 = round((c3/len(sums))*100, 1)

        c4 = sums.count(4)
        p4 = round((c4/len(sums))*100, 1)
        
        print("Game {}:".format(i))
        print(" Group A: {} ({}%); Group B: {} ({}%); Prof: {} ({}%)".format(groupAWins, p2, groupBWins, p4, profWins, p3))
    return groupAWins, groupBWins, profWins

#function that will determine each of the total wins

def totalWins(groupAWins, groupBWins, profWins):
    groupATotalWins = 0
    groupBTotalWins = 0
    profTotalWins = 0
    for i in range (0, n):
        if (groupAWins > groupBWins and groupAWins > profWins):
            groupATotalWins += 1
        if (groupBWins > groupAWins and groupBWins > profWins):
            groupBTotalWins += 1
        if (profWins > groupAWins and profWins > groupBWins):
            profTotalWins += 1
        if (groupAWins == groupBWins == profWins):
            random.random(groupAWins, groupBWins, profWins)+1
        if (groupAWins == groupBWins and (groupAWins == groupBWins) > profWins):
            random.random(groupAWins, groupBWins)+1
        if (groupAWins == profWins and (groupAWins == profWins) > groupBWins):
            random.random(groupAWins, profWins)+1
        if (groupBWins == profWins and (groupBWins == profWins) > groupAWins):
            random.random(groupBWins, profWins)+1
        pA =round((groupATotalWins/n)*100)
        pB =round((groupBTotalWins/n)*100)
        pP =round((profTotalWins/n)*100)
    return groupATotalWins, groupBTotalWins, profTotalWins, pA, pB, pP

# main part of function

n = int(input("How many games? "))
k = int(input("How many coin tosses per game? "))
groupAWins, groupBWins, profWins = gameNumPrint()
groupATotalWins, groupBTotalWins, profTotalWins, pA, pB, pP = totalWins(groupAWins, groupBWins, profWins)
print("Wins: Group A = {} ({}%); Group B = {} ({}%); Prof = {} ({}%)".format(groupATotalWins, pA, groupBTotalWins, pB, profTotalWins, pP))
    

        
