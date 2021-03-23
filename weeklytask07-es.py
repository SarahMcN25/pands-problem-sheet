# This program reads a text file from the argument line
# and outputs how many e's it contains
# Author: Sarah McNelis

import sys # importing this module in oder to call filename from argument line
filename = sys.argv[1]

def letterFreq(filename, letter): 
    # I decided to write this as a function so it could be used again in another prog
    with open(filename, encoding="utf-8") as f:
        # when opening the file here I added encloding 
        # this is because the text file may have different encoding method to my system
        letterCount = f.read().count(letter) 
        # reading whole file and counting the chosen letter
        return letterCount

print(letterFreq(filename, 'e'))
# calling the function here
