# this program reads a text file and outputs how many e's it contains
# Author: Sarah McNelis

# https://manybooks.net/titles/melvilleetext01moby11.html
# https://www.w3schools.com/python/ref_string_count.asp

# **** cannot get this to work with moby-dick.txt but works for test.txt????
# why?????????

import sys
filename = sys.argv[1]

#option 1
with open(filename) as f:
    letter = f.read().count("e")
    print(letter)

'''
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
print(letterFrequency('mbd.txt', 'e')) 

#option 3
count = 0
char = ("e")
file = open("moby-dick.txt","rt")
for i in file:
  for c in i:
    if c == char:
      count = count + 1
print("THE CHARACTER {} IS FOUND {} TIMES IN THE TEXT FILE".format(char,count))

# Program to get letter count in a text file 
  
# explit function to return the letter count 
def letterFrequency(fileName, letter): 
    # open file in read mode 
    file = open(fileName, "rt") 
  
    # store content of the file in a variable 
    text = file.read() 
  
    # declare count variable 
    count = 0
  
    # iterate through each character 
    for char in text: 
  
        # compare each character with 
        # the given letter 
        if char == letter: 
            count += 1
  
    # return letter count 
    return count 
  
  
# call function and display the letter count 
print(letterFrequency('moby-dick.txt', 'e')) 
'''