# This program takes in a positive floating point number 
# then outputs an approximation of it's square root 
# catch = without using built in functions
# Author: Sarah McNelis

num = float(input("Please enter a positive number: "))

# make own function here using: 
# newton's formula: √ N ≈ ½(N/A + A)
def newtonsqrt(num):
    guess = num #using input number as the first guess
    for i in range(10): #for loop to create iteration
        newguess = (((num / guess) + guess) / 2) 
        guess = newguess #will loop again using newguess as guess giving a different newguess
    return round(newguess, 1) #return breaks the for loop

var = newtonsqrt(num)
print ("The square root of {} is approx. {}.".format(num, var))
# calling the function here