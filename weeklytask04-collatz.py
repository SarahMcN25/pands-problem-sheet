# This program asks the user to input any positive integer
# then outputs the succesive value of the following
# if an even number it's divided my two
# if an odd number it's multiplied by three plus one
# Author: Sarah McNelis

numberfrom = int(input("Please enter a positive integer:"))
numlist = []
numlist.append(numberfrom) # this adds the numberFrom to the list above

while numberfrom != 1: # this will stop the loop at number 1
    if numberfrom % 2 == 0: 
        # if the remainder is equal to zero which is true it will run the next line 
        # if false it will run the else statement
        numberfrom = int(numberfrom // 2)
    else: 
        numberfrom = int((numberfrom * 3) + 1) # will run this if the if statement is false
    numlist.append(numberfrom) # this adds all calculations to the numList

print (numlist) # this will print the new list