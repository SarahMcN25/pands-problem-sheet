# pands-problem-sheet README.md
# Author: Sarah McNelis


## **References from the following books:**
### - Sweigart, A 2015, *Automate The Boring Stuff with Python*, William Pollock, San Francisco.
### - VanderPlas, J 2016, *A Whirlwind Tour of Python*, O’Reilly Medica Inc, Sebastopol.
### - <<https://www.w3schools.com/default.asp>>
### - <<https://www.kite.com/>> 
### - <<https://www.tutorialexample.com/>> 
### - <<https://matplotlib.org/stable/index.html>>
### - <<https://www.geeksforgeeks.org/>>

# **weeklytask02-bmi.py**
### - Using a string when calculating to differentiate where a string begins and ends (Sweigart 2015, p. 17)
### - This allows the program to calculate the height from cm into meters squared before calculating the bmi
### - Using / for a true division which includes the decimal place (Sweigart 2015, p. 15)(VanderPlas 2016, p. 18)
### - Using ** for exponentiation which will calculate m squared (Sweigart 2015, p. 15)(VanderPlas 2016, p. 18)
### - Need to use float() instead of int() to allow for a decimal place in answer (VanderPlas 2016, p. 25)
### - Originally used int which calculated incorrectly because it didn’t include the decimal place
### - When developing the code I checked that it worked as I went along bit by bit
### - I’ve left these in this program and put a # before them to remove them from the final code. 
### - This is called >commenting out code (Sweigart 2015, p. 23) 


# **weeklytask03-secondstring.py**
### - > A list is a value that contains multiple values in an ordered sequence (Sweigart 2015, p. 80)
### - Indexing is a means of getting a single value from the list (VanderPlas 2016, p. 33)
### - Python uses zero based indexing therefore the first value in the list is 0 and so on (Sweigart 2015, p. 80)(VanderPlas 2016, p. 32)
### - > Elements at the end of the list can be accessed with negative numbers, starting from -1 (VanderPlas 2016, p. 32) 
### - This is what I used in this program to output the sentence backwards
### - > Slicing is a means of accessing multiple values in sublists (VanderPlas 2016, p. 33) 
### - > It uses a colon to indicate the start point (inclusive) and end point (non-inclusive) of the subarray (VanderPlas 2016, p. 33)
### - Slicing outputs a new string by using parts of the old string (Sweigart 2015, p. 94) <<https://www.w3schools.com/python/python_strings_sclicing.asp>>
### - Using [::-2] means it will show me the full string every second value backwards 


# **weeklytask04-collatz.py**
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


# **weeklytask05-weekday.py**
### - >For loading built-in and third-party modules, Python provides the import statement (VanderPlas 2016, p. 66)
### - This program imports the datetime module (Sweigart 2015, p. 341)
### - This allows python to determine the current date information as date objects <<https://www.w3schools.com/python/python_datetime.asp>>
### - Printing datetime.datetime.now() outputs a datetime object for thecurrent date and time, according to the computers clock (Sweigart 2015, p. 341)
### - Selecting the function strftime() will convert the datetime object into a string (Sweigart 2015, p. 344)
### - Using %A will output the full weekday name as a string (Sweigart 2015, p. 344) <<https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_a2>> 
### - This program uses the if and else statements.
### - If the first statement is true the it will run the code. If it's false it will run the else statment (Sweigart 2015, p. 38, 39)(VanderPlas 2016, p. 40)
### - This is how the program determines if the current day is a weekend or weekday. 

# **weeklytask06-squareroot.py**
### - > A function is like a mini program (Sweigart 2015, p. 61)
### - The code of this mini program/function is only executed when called (Sweigart 2015, p. 62)
### - Functions are used to organise code and make it more readable and resuable (VanderPlas 2016, p. 41)
### - There are two ways of using functions; def statements and lambda statements (VanderPlas 2016, p. 41)
### - A def statment is useful for any type of function wheras a lambda statment is used for creating short anomoyous functions (VanderPlas 2016, p. 41)
### - I have chosen to use a def statement as I want to define and organise my functions so they can be easily accessed and used again (VanderPlas 2016, p. 42)
### - The variables that are written within a function only exist in that function (Sweigart 2015, p. 67)
### - This is somehting that casused a bit of trouble when writing this program. Differiencating bwtween global scope vs local scope. Local scope being within a function. 
### - > Code in global scope cannot use any local variables (Sweigart 2015, p. 67)
### - In other words a variable within a funcation cannot be called on outside the function. One can only call the function itself. 
### - > When an expression is used with a return statement, the return value is what the expression evaluates to (Sweigart 2015, p. 64)
### - In other words you need to think about what you're asking and what the answer would be; the expression/argument and the answer/return value. 
### - For this program I created my own function for calculating approximation of positive floating-point number's square root. 
### - I based my code on Newton's formula; √ N ≈ ½(N/A + A) found at <<https://www.school-for-champions.com/algebra/square_root_approx.htm#.YEkLyU5xfIX>>
### - The idea of Newton's method according to the above website is to use an estaminated guess for A and then repeadedly use the answer in the formula as A until the correct answer is obtained.
### - In this program I decided to divide the input number by 4 as my educated guess.
### - I used a while loop to continue the equation until the statement was true in which case the else block comes into effect (VanderPlas 2016, p. 40)(Sweigart 2015, p. 38, 39)  

# **weeklytask07-es.py**
### - 


# **weeklytask08-plottask.py**
### - This was the most enjoyable task for me. We were told that plots can be a bit of a rabbit hole which I have learned to be true. And I definitely went down the rabbit hole! 
### - I started off having a bit of trouble trying to figure out how I was going to plot three functions on one axis. I got inspiration from this website which brought my thought process back to basics <<https://www.kite.com/python/answers/how-to-make-multiple-plots-on-the-same-figure-in-matplotlib-in-python>>
### - You need to plot an x-axis with a y-axis. So I decided to put the range on the x-axis. Then I broke down the three functions to the ypoints1, 2 and 3. The x-axis stayed the same for all three functions but the y-axis changed. This is how I developed this plot. 
### - W3schools has good tutorials on how to plot a line diagram which I also found quite useful <<https://www.w3schools.com/python/matplotlib_plotting.asp>>
### - Next I looked at line colors. I found this website which contains a list of named colors supported in matplotlib <<https://matplotlib.org/stable/gallery/color/named_colors.html>>
### - This was quite useful when it came to color coordination and design. I played around with different colors until I found a sequence that I was happy with. 
### - As I discovered from this website base colors can be called using the first letter of the color. However, there are also colors from tableau palette and css colors which can be called by using the full name of the color.  
### - After this I started investigating different linesytles. I decied as there were three functions, they should have three different linestyles. For this I looked at the w3schools website. Here I learned about the five linestyles available in matplotlib. This webpage also gave interactive examples on how you can change colors <<https://www.w3schools.com/python/matplotlib_line.asp>>
### - It also describles how you can adjust the thickness of a line diagram using the keyword linewidth or lw <<https://www.w3schools.com/python/matplotlib_line.asp>>
### - After even more research I began putting a title on the plot and labelling the axis' <<https://www.tutorialexample.com/understand-matplotlib-fontdict-a-beginner-guide-matplotlib-tutorial/>>
### - Then I played around with colors, font style, font size and weight for the title and labels. <<https://www.tutorialexample.com/understand-matplotlib-fontdict-a-beginner-guide-matplotlib-tutorial/>> this website has a quite a useful table of fontdict keys and values that are used in python. These keys include family(for font style), color, weight, size and stlye (normal/italic/oblique).
### - Following this I decided to put a legend on the plot. After a bit mroe exploration I found this website which give a substantial amount of detail regarding the parameters around legends <<https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html>>. It was here I discovered how to position a legend and adjust the font size, color and other parameters.
# I have commeted out a bit of code at the end of this program which would save the plot to a file <<https://www.geeksforgeeks.org/how-to-save-a-plot-to-a-file-using-matplotlib/>>