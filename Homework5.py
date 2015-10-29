__author__ = 'Fotty'
from pip.backwardcompat import raw_input
"""
Exercise 1. Celsius and Fahrenheit

Write a program which reads Celsius temperatures from the file temperatures.txt (make this file by yourself),
converts the temperatures to Fahrenheit, and prints out the converted temperatures.
Program should output Invalid input for those lines of file where conversion to number fails for some reason,
and continue with the next line in the file.

"""
xfile = open("temperatures.txt", 'r')

for temp in xfile:
    try:
        c = str(temp).strip()
        f = (str(float(temp) * 9/5 + 32))
        print("Celsius: %s Fahrenheit: %s" %(c, f))
        #Celsius: 32.0 Fahrenheit: 89.6

    except:
        print("Invalid input")



"""
Exercise 2. Numbered lines
Write a program which prompts the user for filename and outputs all lines from the file with the line number.
Make sure that program works nicely with all files which exist and do not exist (use try-except)."""



try:
    question = raw_input('Enter the name of the file to read: ')
    xxfile = open(question, 'r')
    var = 0
    for txt in xxfile:
        acc = txt.strip()
        var += 1
        print(str(var)+ "." + acc)

except:
        print("The file is empty or it might be missing :( ")

