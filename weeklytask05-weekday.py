# This program outputs whether or not today is a weekday
# Author: Sarah McNelis

weekend = ["Saturday", "Sunday"]

import datetime # importing this module in order to access current date/time as an object
x = datetime.datetime.now() # this will give current date/time as per my pc's clock
x.strftime("%A")
# strftime converts into a string
# %A access the actual word of which day it is

if x != weekend:
    print("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")
#using and if and else statements here. Once determined above what day is it
# if it's not the weekend it will print from the if statement
# when the if statment is false it will run the else statment