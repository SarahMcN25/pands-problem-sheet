# pands-problem-sheet README.md
# Author: Sarah McNelis


## **References from the following books:**
### - Sweigart, A 2015, *Automate The Boring Stuff with Python*, William Pollock, San Francisco.
### - VanderPlas, J 2016, *A Whirlwind Tour of Python*, O’Reilly Medica Inc, Sebastopol.
### - <<https://www.w3schools.com/default.asp>>


# **1. weeklytask02-bmi.py**
### - Using a string when calculating to differentiate where a string begins and ends (Sweigart 2015, p. 17)
### - This allows the program to calculate the height from cm into meters squared before calculating the bmi
### - Using / for a true division which includes the decimal place (Sweigart 2015, p. 15)(VanderPlas 2016, p. 18)
### - Using ** for exponentiation which will calculate m squared (Sweigart 2015, p. 15)(VanderPlas 2016, p. 18)
### - Need to use float() instead of int() to allow for a decimal place in answer (VanderPlas 2016, p. 25)
### - Originally used int which calculated incorrectly because it didn’t include the decimal place
### - When developing the code I checked that it worked as I went along bit by bit
### - I’ve left these in this program and put a # before them to remove them from the final code. 
### - This is called >commenting out code (Sweigart 2015, p. 23) 


# **2. weeklytask03-secondstring.py**
### - > A list is a value that contains multiple values in an ordered sequence (Sweigart 2015, p. 80)
### - Indexing is a means of getting a single value from the list (VanderPlas 2016, p. 33)
### - Python uses zero based indexing therefore the first value in the list is 0 and so on (Sweigart 2015, p. 80)(VanderPlas 2016, p. 32)
### - > Elements at the end of the list can be accessed with negative numbers, starting from -1 (VanderPlas 2016, p. 32) 
### - This is what I used in this program to output the sentence backwards
### - > Slicing is a means of accessing multiple values in sublists (VanderPlas 2016, p. 33) 
### - > It uses a colon to indicate the start point (inclusive) and end point (non-inclusive) of the subarray (VanderPlas 2016, p. 33)
### - Slicing outputs a new string by using parts of the old string (Sweigart 2015, p. 94) <<https://www.w3schools.com/python/python_strings_sclicing.asp>>
### - Using [::-2] means it will show me the full string every second value backwards 


# **3. weeklytask04-collatz.py**
### - A Boolean is a data type which only has two values > true and false (Sweigart 2015, p. 32)(VanderPlas 2016, p. 29)
### - This program uses comparison operators such as not equal to (!=) which gives one of the boolean values true and false (VanderPlas 2016, p. 20, 21)(Sweigart 2015, p. 33)
### - This program uses math/arithmetic operators such as remainder, floor division, multiply and add (Sweigart 2015, p. 15)(VanderPlas 2016, p. 18)
### - using remainder identifies if the number is even or odd. If the remainder is equal to zero then it run the next piece of code.
### - The while statement will run as long as the while statement's condition is true (Sweigart 2015, p. 45)
### - Therefore by adding the statement 'while numberFrom != 1:' the loop will stop or be considered false once it reaches the number 1.
### - The block following an if statement will run if the statement is true (Sweigart 2015, p. 38)
### - The else block only runs if all the if and elif statments are false (VanderPlas 2016, p. 40)(Sweigart 2015, p. 39)
### - using append() will add the new values to the pointed list (Sweigart 2015, p. 89)
### - In this program it will add the values from numberFrom to the designated list which is numList hense numlist.append(numberFrom)


# **4. weeklytask05-weekday.py**
### - >For loading built-in and third-party modules, Python provides the import statement (VanderPlas 2016, p. 66)
### - This program imports the datetime module (Sweigart 2015, p. 341)
### - This allows python to determine the current date information as date objects <<https://www.w3schools.com/python/python_datetime.asp>>
### - Printing datetime.datetime.now() outputs a datetime object for thecurrent date and time, according to the computers clock (Sweigart 2015, p. 341)
### - Selecting the function strftime() will convert the datetime object into a string (Sweigart 2015, p. 344)
### - Using %A will output the full weekday name as a string (Sweigart 2015, p. 344) <<https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_a2>> 
### - This program uses the if and else statements.
### - If the first statement is true the it will run the code. If it's false it will run the else statment (Sweigart 2015, p. 38, 39)(VanderPlas 2016, p. 40)
### - This is how the program determines if the current day is a weekend or weekday. 