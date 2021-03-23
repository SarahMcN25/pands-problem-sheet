# This program asks the user to input any positive integer
# then outputs the succesive value of the following
# if an even number it's divided my two
# if an odd number it's multiplied by three plus one
# Author: Sarah McNelis

numberFrom = int(input("Please enter a positive integer:"))
numList = []
numList.append(numberFrom) # this adds the numberFrom to the list above

while numberFrom != 1: # this will stop the loop at number 1
    if numberFrom % 2 == 0: 
        # if the remainder is equal to zero which is true it will run the next line 
        # if false it will run the else statement
        numberFrom = int(numberFrom // 2)
    else: 
        numberFrom = int((numberFrom * 3) + 1) # will run this if the if statement is false
    numList.append(numberFrom) # this adds all calculations to the numList

print (numList) # this will print the new list