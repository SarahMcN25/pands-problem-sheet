# pands-problem-sheet README.md
# Author: Sarah McNelis

## **References from the following books:**
### - Sweigart, A 2015, *Automate The Boring Stuff with Python*, William Pollock, San Francisco.
### - VanderPlas, J 2016, *A Whirlwind Tour of Python*, O’Reilly Medica Inc, Sebastopol.

# **1. weeklytask02-bmi.py**
### - Using a string when calculating to differentiate where a string begins and ends (VanderPlas 2016, p. 17)
### - This allows the program to calculate the height from cm into meters squared before calculating the bmi
### - Using / for a true division which includes the decimal place (Sweigart 2015, p. 18)(VanderPlas 2016, p. 15)
### - Using ** for exponentiation which will calculate m squared (Sweigart 2015, p. 18) (VanderPlas 2016, p. 15)
### - Need to use float() instead of int() to allow for a decimal place in answer (Sweigart 2015, p. 25)
### - I originally used int which calculated incorrectly because it didn’t include the decimal place
### - When developing the code I checked that it worked as I went along bit by bit
### - I’ve left these in the program and put a # before them to remove them from the final code. 
### - This is called >commenting out code (VanderPlas 2016, p. 23) 

# **2. weeklytask03-secondstring.py**
### - > A list is a value that contains multiple values in an ordered sequence (VanderPlas 2016, p. 80)
### - Indexing is a means of getting a single value from the list (Sweigart 2015, p. 33)
### - Python uses zero based indexing therefore the first value in the list is 0 and so on (Sweigart 2015, p. 32)(VanderPlas 2016, p. 80)
### - > Elements at the end of the list can be accessed with negative numbers, starting from -1 (Sweigart 2015, p. 33) 
### - This is what I used in this program to output the sentence backwards
### - > Slicing is a means of accessing multiple values in sublists (Sweigart 2015, p. 33) 
### - > It uses a colon to indicate the start point (inclusive) and end point (non-inclusive) of the subarray (Sweigart 2015, p. 33)
### - Slicing outputs a new string by using parts of the old string (VanderPlas 2016, p. 94)
### - Using [::-2] means it will show me the full string every second value backwards 

# **3. weeklytask04-collatz.py**
### - A Boolean is a data type which only has two values > true and false (Sweigart 2015, p. 32)(VanderPlas 2016, p. 29)
### - This program uses comparison operators such as not equal to (!=) which gives one of the boolean values true and false (VanderPlas 2016, p. 20, 21)
### - > Comparison operators compare two values and evaluate down to a single Boolean value (Sweigart 2015, p. 33)
### - This program uses math/arithmetic operators such as remainder, floor division, multiply and add (Sweigart 2015, p. 15)(VanderPlas 2016, p. 17, 18)
### - using remainder identifies if the number is even or odd. If the remainder is equal to zero then it run the next piece of code.
### - The while statement will run as long as the while statement's condition is true (Sweigart 2015, p. 45)
### - Therefore by adding the statement 'while numberFrom != 1:' the loop will stop or be considered false once it reaches the number 1.
### - The block following an if statement will run if the statement is true (Sweigart 2015, p. 38)
### - The else block only runs if all the if and elif statments are false (VanderPlas 2016, p. 40)(Sweigart 2015, p. 39)
### - This is how it differentiates the even from the odd numbers in this program. If it's true it will divide the even number. If false it will move to the else statement and run that calculation instead. 
### - using append() will add the new values to the pointed list (Sweigart 2015, p. 89)(VanderPlas 2016, p. 15)
### - In this program it will add the values from numberFrom to the designated list which is numList hense numlist.append(numberFrom)

# **4. weeklytask05-     .py**