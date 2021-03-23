# This program reads a text file from the argument line
# and outputs how many e's it contains
# Author: Sarah McNelis

import sys
filename = sys.argv[1]

#option 1
def letterFreq(filename, letter): 
    with open(filename, encoding="utf-8") as f:
        letterCount = f.read().count(letter)
        return letterCount

print(letterFreq(filename, 'e'))


# Option 2 and 3 are other ways of writing this program
'''
#option 2
with open(filename, encoding="utf-8") as f:
    letter = f.read().count("e")
    print(letter)


#option 3
def letterFreq(filename, letter): 
    with open(filename, encoding="utf-8") as f: 
        txt = f.read() 
        return txt.count(letter) 
  
print(letterFreq(filename, 'e')) 
'''
 