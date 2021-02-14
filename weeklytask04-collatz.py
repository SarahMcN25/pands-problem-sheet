# this program asks the user to input any positive integer
# then outputs the succesive value of:
# if even number its divided my two
# if odd number its multiplied by three plus one
# Author: Sarah McNelis


numberFrom = int(input("Please enter a positive integer:"))
numList = []
numList.append(numberFrom)

while numberFrom != 1:
    if numberFrom % 2 == 0:
        numberFrom = int(numberFrom // 2)
    else: 
        numberFrom = int((numberFrom * 3) + 1)
    numList.append(numberFrom)

print (numList)

