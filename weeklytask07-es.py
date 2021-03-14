# this program reads a text file and outputs how many e's it contains
# Author: Sarah McNelis

# https://manybooks.net/titles/melvilleetext01moby11.html
# https://www.w3schools.com/python/ref_string_count.asp

# **** cannot get this to work with moby-dick.txt but works for test.txt????
# why?????????

#option 1
#with open("MobyD.txt", "rt") as f:
    #letter = f.read().count("e")
    #print(letter)
       
#option 2
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# Program to get letter count in a text file 
# explit function to return the letter count 
def letterFrequency(fileName, letter): 
    # open file in read mode 
    file = open(fileName, 'rt') 
  
    # store content of the file in a variable 
    text = file.read() 
  
    # using count() 
    return text.count(letter) 
  
  
# call the function and display the letetr count 
print(letterFrequency('moby-dick.txt', 'e')) 