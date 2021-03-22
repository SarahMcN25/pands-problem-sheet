# this program reads in a text file and outputs how many e's it contains
# Author: Sarah McNelis

# type txt filename into argument line: python es.py moby-dick.txt
import sys
filename = sys.argv[1]

with open(filename) as f:
    letter = f.read().count("e")
    print(letter)


#option 1
with open("test.txt", "rt") as f:
    letter = f.read().count("e")
    print(letter)



#option 2
def letterFrequency(fileName, letter): 
    file = open(fileName, 'rt') 
    text = file.read() 
    return text.count(letter) 
  
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


#option4
def letterFrequency(fileName, letter): 
    file = open(fileName, "rt") 
    text = file.read() 
    count = 0
    for char in text:  
        if char == letter: 
            count += 1
    return count 
  
print(letterFrequency('moby-dick.txt', 'e')) 

