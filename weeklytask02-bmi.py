# This program inputs a person's height in cm and weight in kg
# then outputs their bmi (weight divided by height) in meters squared
# Author: Sarah McNelis

weight = float(input("Enter weight(kg):"))
#print ('weight') 

height = float(input("Enter height(cm):"))
#print ('height') 

newheight = ((height/100)**2)
#print (newHeight)

bmi = (weight/newheight)
#print (bmi) 

print ("BMI is: {}".format(bmi))
