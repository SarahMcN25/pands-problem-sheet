# This program outputs whether or not today is a weekday
# Author: Sarah McNelis

import datetime # importing this module in order to access current date/time as an object
x = datetime.datetime.now() # this will give current date/time as per my pc's clock
today = x.strftime("%A")
#print(today)
# strftime converts into a string
# %A access the actual word of which day it is

if today == 'Saturday':
    print("It is the weekend, yay!")
elif today == 'Sunday':
    print("It is the weekend, yay!")  
else:
    print("Yes, unfortunately today is a weekday.")
# using an if and else statements here. Once determined above what day is it
# if it is Saturday it will print from the if statement
# if it is SUnday it will print from the elif statement
# otherwise it will run the else statment