# this program takes in a positive floating point number 
# then outputs an approximation of it's square root 
# without using built in functions
# Author: Sarah McNelis

num = float(input("Please enter a positive number: "))

def newtonSqrt(num):
    a = (num/4)
    sqRoot = (((num / a) + a) / 2)
    x = sqRoot * sqRoot
    while x != num:
        sqRoot2 = (((num / sqRoot) + sqRoot) /2)
        return round(sqRoot2, 1)
    else:
        return round(sqRoot, 1)
# used an educated guess to divide input num by 4. 
# then while loop until square root ans multiplied by itself is equal to input num

var = newtonSqrt(num)
print ("The square root of {} is approx. {}.".format(num, var))