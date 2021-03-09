# this program takes in a positive floating point number 
# then outputs an approximation of it's square root 
# without using built in functions
# Author: Sarah McNelis

## https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD5KOdNCfIW



num = float(input("Please enter a positive number: "))

def newtonSqrt(num):
    a = float(num / 2)
    sqRoot = float(((num / a) + a) / 2)
    return sqRoot
    

var = newtonSqrt(num)
print ("The square root of {} is approx. {}".format(num, var))

### need to come back to this. think i need a while loop in function
### sqRoot * sqRoot should be equals to num?? 
### how can I write this??? 

