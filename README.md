# PANDS-PROBLEM-SHEET README.MD
# Author: Sarah McNelis


## **REFERENCES AND RESOURCES USED:**
### - Sweigart, A 2015, *Automate The Boring Stuff with Python*, William Pollock, San Francisco.
### - VanderPlas, J 2016, *A Whirlwind Tour of  Python*, O’Reilly Medica Inc, Sebastopol.
### - <<https://www.w3schools.com/default.asp>>
### - <<https://www.kite.com/>> 
### - <<https://www.tutorialexample.com/>> 
### - <<https://matplotlib.org/stable/index.html>>
### - <<https://www.geeksforgeeks.org/>>
### - <<https://www.w3.org/>> 
### - <<https://www.python.org/>>
### - <<https://www.pitt.edu/~naraehan/python3/mbb12.html>>
### - <<https://stackoverflow.com/>>
### - <<https://manybooks.net/>>
### - <<http://gutenberg.org/>>
### - <<https://www.pythonforbeginners.com/>>
### - <<https://www.pythontutorial.net/>>   


# **WEEKLYTASK02-BMI.PY**
### - solution to week 02
### - this is to calculate body mass index....
### -  add references and code here
### - Using a string when calculating to differentiate where a string begins and ends (Sweigart 2015, p. 17)
### - This allows the program to calculate the height from cm into meters squared before calculating the bmi
### - Using / for a true division which includes the decimal place (Sweigart 2015, p. 15)(VanderPlas 2016, p. 18)
### - Using ** for exponentiation which will calculate m squared (Sweigart 2015, p. 15)(VanderPlas 2016, p. 18)
### - Need to use float() instead of int() to allow for a decimal place in answer (VanderPlas 2016, p. 25)
### - Originally used int which calculated incorrectly because it didn’t include the decimal place
### - When developing the code I checked that it worked as I went along bit by bit
### - I’ve left these in this program and put a # before them to remove them from the final code. 
### - This is called >commenting out code (Sweigart 2015, p. 23) 


# **WEEKLYTASK03-SECONDSTRING.PY**
### - > A list is a value that contains multiple values in an ordered sequence (Sweigart 2015, p. 80)
### - Indexing is a means of getting a single value from the list (VanderPlas 2016, p. 33)
### - Python uses zero based indexing therefore the first value in the list is 0 and so on (Sweigart 2015, p. 80)(VanderPlas 2016, p. 32)
### - > Elements at the end of the list can be accessed with negative numbers, starting from -1 (VanderPlas 2016, p. 32) 
### - This is what I used in this program to output the sentence backwards
### - > Slicing is a means of accessing multiple values in sublists (VanderPlas 2016, p. 33) 
### - > It uses a colon to indicate the start point (inclusive) and end point (non-inclusive) of the subarray (VanderPlas 2016, p. 33)
### - Slicing outputs a new string by using parts of the old string (Sweigart 2015, p. 94) <<https://www.w3schools.com/python/python_strings_sclicing.asp>>
### - Using [::-2] means it will show me the full string every second value backwards 


# **WEEKLYTASK04-COLLATZ.PY**
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


# **WEEKLYTASK05-WEEKDAY.PY**
### - >For loading built-in and third-party modules, Python provides the import statement (VanderPlas 2016, p. 66)
### - This program imports the datetime module (Sweigart 2015, p. 341)
### - This allows python to determine the current date information as date objects <<https://www.w3schools.com/python/python_datetime.asp>>
### - Printing datetime.datetime.now() outputs a datetime object for thecurrent date and time, according to the computers clock (Sweigart 2015, p. 341)
### - Selecting the function strftime() will convert the datetime object into a string (Sweigart 2015, p. 344)
### - Using %A will output the full weekday name as a string (Sweigart 2015, p. 344) <<https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_a2>> 
### - This program uses the if and else statements.
### - If the first statement is true the it will run the code. If it's false it will run the else statment (Sweigart 2015, p. 38, 39)(VanderPlas 2016, p. 40)
### - This is how the program determines if the current day is a weekend or weekday. 


# **WEEKLYTASK06-SQUAREROOT.PY**
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


# **WEEKLYTASK07-ES.PY**
### - For this task I got the moby-dick text file from <<http://gutenberg.org/ebooks/2701>>
### - I have chosen complete this task using a function. I've done this to give me the option to use this function again by importing it into another program.
### - The instruction for this task was to call the filename from an argument on the command line. I discovered you need to first import the sys module. <<https://www.pythonforbeginners.com/system/python-sys-argv>>
### - In this case the user enters in the filename on the command line while running the program. This creates a list of arguments that then run through the program. <<https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script>>
### - I have used: filename = sys.argv[1]. This means I want to use the filename of the first argument in the command line. 
### - This program required the use of the string count method which allows it to count all the letter e's. <<https://www.w3schools.com/python/ref_string_count.asp>>
### - I should note here that I interperted the task as if it wanted the number of lowercase e's.
### - I also found some code on <<https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/>>
### - This example inspired my own efforts for my program. It shows how you open a file in read mode, read it counting the amount of occurences an e was used. 
### - This website also describes different methods of reading a file. I choose to used read() which reads in the full text into a string for manipulation. <<https://www.pythontutorial.net/python-basics/python-read-text-file/#:~:text=To%20read%20a%20text%20file%20in%20Python%2C%20you,the%20file%20using%20the%20file%20close%20%28%29%20method>>
### - This task was quite challenging when I started to run my program. It brought me to do a lot of research on errors. 
### - I kept getting the following error "UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 10533: character maps to <undefined>"
### - At first I thought maybe it was an issue with the specific text file. So I found a different one from another website <<https://manybooks.net/titles/melvilleetext01moby11.html>>
### - Again the same issue. I already knew it wasn't my code as I ran it using a test text file I created myself so I decided to google the error and started my research.
### - These websites suggest that the text files may have a different encoding method to that of my system's default encoding. <<https://www.pitt.edu/~naraehan/python3/mbb12.html>> <<https://stackoverflow.com/questions/49562499/how-to-fix-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-posit>>
### - These two websites both suggest using an encoding switch which ellimate the error eg. encoding="utf-8". This stands for 8 bit unicode.
### - Unicode is defined as a specification that aims to list every character used by human languages and give each character its own unique code. <<https://docs.python.org/3/howto/unicode.html>>
### - The following website explains that "utf-8" should be used for web content. <<https://www.w3.org/International/questions/qa-choosing-encodings>>
### - When opening the read I added encoding="utf-8" after the filename which decoded the file allowing the program to run.


# **WEEKLYTASK08-PLOTTASK.PY**
### - This was the most enjoyable task for me. We were told that plots can be a bit of a rabbit hole which I have learned to be true. And I definitely had a lot of fun exploring!
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
### - I have commeted out a bit of code at the end of this program which would save the plot to a file <<https://www.geeksforgeeks.org/how-to-save-a-plot-to-a-file-using-matplotlib/>>