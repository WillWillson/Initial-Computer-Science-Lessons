######################################################################################################################
# Name: William Wilson
# Date: 12/16/2020
# Description: This program will give a list, and will be sorted using different methods
######################################################################################################################
from random import randint, seed
# creates the list using the seed provided by the user
def getList():
        seed(theseed)
        mylist = []
        for i in range(1, 10):
            mylist.append(randint(1, 100))
        return mylist


# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bubbleSort(numbers):
        print("The list: {}".format(numbers))
        n = len(numbers)
        totalSwaps = 0
        totalComparisons = 0
        for i in range(1, n):
                swaps = 0
                comparisons = 0
                for j in range(1, n - i + 1):
                        comparisons += 1
                        if (numbers[j] < numbers[j - 1]):
                                temp = numbers[j]
                                numbers[j] = numbers[j - 1]
                                numbers[j - 1] = temp
                                swaps += 1
                totalSwaps = totalSwaps + swaps
                totalComparisons = totalComparisons + comparisons
        print("After bubble sort {}".format(numbers))
        return totalComparisons, totalSwaps

# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optimizedBubbleSort(numbers2):
        print("The list: {}".format(numbers2))
        n = len(numbers2)
        totalSwaps = 0
        totalComparisons = 0
        for i in range(1, n):
                swaps = 0
                comparisons = 0
                noSwaps = True
                for j in range(1, n - i + 1):
                        comparisons += 1
                        if (numbers2[j] < numbers2[j - 1]):
                                temp = numbers2[j]
                                numbers2[j] = numbers2[j - 1]
                                numbers2[j - 1] = temp
                                swaps += 1
                                noSwaps = False
                totalSwaps = totalSwaps + swaps
                totalComparisons = totalComparisons + comparisons
        print("After optimized bubble sort: {}".format(numbers2))
        return totalComparisons, totalSwaps

# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selectionSort(numbers3):
        print("The list: {}".format(numbers3))
        n = len(numbers3)
        totalSwaps = 0
        totalComparisons = 0
        for i in range(0, n - 1):
                minPosition = i
                for j in range(i + 1, n):
                        if (numbers3[j] < numbers3[minPosition]):
                                minPosition = j
                        totalComparisons += 1
                temp = numbers3[i]
                numbers3[i] = numbers3[minPosition]
                numbers3[minPosition] = temp
                totalSwaps += 1
        print("After selection sort: {}".format(numbers3))
        return totalComparisons, totalSwaps

# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insertionSort(numbers4):
        print("The list: {}".format(numbers4))
        n = len(numbers4)
        totalSwaps = 0
        totalComparisons = 0
        i = 1
        while (i < n):
                comparisons = 1
                swaps = 0
                if(numbers4[i - 1] > numbers4[i]):
                        temp = numbers4[i]
                        j = i - 1
                        while (j >= 0 and numbers4[j] > temp):
                                comparisons += 1
                                numbers4[j + 1] = numbers4[j]
                                j -= 1
                                swaps += 1
                        numbers4[j + 1] = temp
                i += 1
                totalComparisons = totalComparisons + comparisons
                totalSwaps = totalSwaps + swaps
        print("After insertion sort: {}".format(numbers4))
        return totalComparisons, totalSwaps

# the main part of the program
theseed = input("What do you want to use as the seed? ")
# insert your main code below.
numbers = getList()
mainComparisons, mainSwaps = bubbleSort(numbers)
print("{} comparisons, {} swaps".format(mainComparisons, mainSwaps))
print(" ")

numbers2 = getList()
comparisons, swaps = optimizedBubbleSort(numbers2)
print("{} comparisons, {} swaps".format(comparisons, swaps))
print(" ")

numbers3 = getList()
mainComparisons, mainSwaps = selectionSort(numbers3)
print("{} comparisons, {} swaps".format(mainComparisons, mainSwaps))
print(" ")

numbers4 = getList()
mainComparisons, mainSwaps = insertionSort(numbers4)
print("{} comparisons, {} swaps".format(mainComparisons, mainSwaps))
print(" ")
