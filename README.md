# pands-problem-sheet README.md
# author: Sarah McNelis

## **References from the following books:**
### - Sweigart, A 2015, *Automate The Boring Stuff with Python*, William Pollock, San Francisco.
### - VanderPlas, J 2016, *A Whirlwind Tour of Python*, O’Reilly Medica Inc, Sebastopol.

# **1. bmi.py**
### - Using a string when calculating to differentiate where a string begins and ends (VanderPlas 2016, p. 17)
### - This allows the program to calculate the height from cm into meters squared before calculating the bmi
### - Using / for a true division which includes the decimal place (Sweigart 2015, p. 18)(VanderPlas 2016, p. 15)
### - Using ** for exponentiation which will calculate m squared (Sweigart 2015, p. 18) (VanderPlas 2016, p. 15)
### - Need to use float() instead of int() to allow for a decimal place in answer (Sweigart 2015, p. 25)
### - I originally used int which calculated incorrectly because it didn’t include the decimal place
### - When developing the code I checked that it worked as I went along bit by bit
### - I’ve left these in the program and put a # before them to remove them from the final code. 
### - This is called >commenting out code (VanderPlas 2016, p. 23) 

# **2. secondstring.py**
### - > A list is a value that contains multiple values in an ordered sequence (VanderPlas 2016, p. 80)
### - Indexing is a means of getting a single value from the list (Sweigart 2015, p. 33)
### - Python uses zero based indexing therefore the first value in the list is 0 and so on (Sweigart 2015, p. 32)(VanderPlas 2016, p. 80)
### - > Elements at the end of the list can be accessed with negative numbers, starting from -1 (Sweigart 2015, p. 33) 
### - This is what I used in this program to output the sentence backwards
### - > Slicing is a means of accessing multiple values in sublists (Sweigart 2015, p. 33) 
### - > It uses a colon to indicate the start point (inclusive) and end point (non-inclusive) of the subarray (Sweigart 2015, p. 33)
### - Slicing outputs a new string by using parts of the old string (VanderPlas 2016, p. 94)
### - Using [::-2] means it will show me the full string every second value backwards 
