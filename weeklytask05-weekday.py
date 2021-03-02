# this program outputs whether or not today is a weekday
# Author: Sarah McNelis

weekend = ["Saturday", "Sunday"]

import datetime
x = datetime.datetime.now()
x.strftime("%A")

if x != weekend:
    print("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")
