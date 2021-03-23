# This program takes in a positive floating point number 
# then outputs an approximation of it's square root 
# catch = without using built in functions
# Author: Sarah McNelis

num = float(input("Please enter a positive number: "))

# make own function here using 
# newton's formula: √ N ≈ ½(N/A + A)
def newtonSqrt(num):
    a = (num/4) 
    # newton's method includes making an educated guess of what a is
    # decided to divide the input number by 4
    sqRoot = (((num / a) + a) / 2)
    x = sqRoot * sqRoot
    while x != num:
        sqRoot2 = (((num / sqRoot) + sqRoot) /2)
        return round(sqRoot2, 1)
    else:
        return round(sqRoot, 1)
# used while loop so that it will continue to calculate the est square root
# until the square root multiplied by itself is equal to input num

var = newtonSqrt(num)
print ("The square root of {} is approx. {}.".format(num, var))
# calling the function here