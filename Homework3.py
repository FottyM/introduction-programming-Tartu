__author__ = 'Fortunat Mutunda'
from pip._vendor.distlib.compat import raw_input
"""
Write a program which prompts the user for one integer number and prints out the part of multiplication table
for the entered number (i.e. the entered number is multiplied with numbers 1-9 and all obtained numbers are output).

Run the program repeatedly to test the various different values for input.

Here are some examples of program output.
"""
num = int(raw_input("A number please: "))
for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
    print(num, "*", i, " = ", num*i)

num1 = 1
num2 = int(raw_input("A number to be multiplied: "))
while num1 <= 12:
    print(num2, "*", num1, " = ", num1*num2)
    num1 += 1
"""
Rewrite the number of days in months program from the previous week adding loop which repeatedly asks numbers of months
and tells the number of days in that month until the user enters “done”. Do not check for leap year
(lets say that number of days in february is always 28).
If the user enters anything other than a number,
detect their mistake using try and except and print an error message and skip to the next number.

Here is an example of program output.
"""

def number_of_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return ("This month has 31 days ")

    elif month == 4 or month == 6 or month == 9 or month == 11:
        return ("This month has 30 days")

    elif month == 2:
        leap_year = int(raw_input("Enter a year then we will tell you if feb has 28 or 29 days: "))

        if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
            return ("Leap year 29 days")

        else:
            return ("Normal year just 28 days")

    else:
        return ("A number between 1-12 please")

while True:
    month = raw_input("Enter a number between 1-12 or word 'done': ")
    if month == 'done':
        break

    try:
        x = int(month)
        m = number_of_days(x)
        print(m)


    except:
        print("a number please ")