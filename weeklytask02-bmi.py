# this program inputs a person's height in cm and weight in kg
# then outputs their bmi (weight divided by height) in meters squared
# author: Sarah McNelis

# need to use variable float instead of int 
# the output implies there might be a float (decimal place)

weight = float(input("Enter weight(kg):"))
#print ('weight') to check code is working

height = float(input("Enter height(cm):"))
#print ('height') to check code is working

newHeight = float((height/100)**2)
#print (newHeight) This converts height from cm to meters squared

bmi = float(weight/newHeight)
#print (bmi) to check calculations are working

print ("BMI is: {}".format(bmi))
