__author__ = 'Fotty'
from pip._vendor.distlib.compat import raw_input

'''
Write a program that asks the number of the month from the user and outputs the number of days in that month.
If you can (and it is not very difficult at all) try to also check for leap years.
In that case you have to also ask the user for the year. If you can’t do it, don’t worry, do it without leap years,
but we encourage you to try! Also make sure that when user inputs some nonsense,
the program gives some feedback about it. You can check it with try-except.

How to check for leap years:
Leap year is a year that is divisible by 4 and is not divisible by 100 or when it is divisible by 400.
This description might be helpful when trying to program it:
If the year is not exactly divisible by 4 then it is a common year.
If it is divisible by 4 we can check is it divisible by 100. If it is not, then it is a leap year.
If it is divisible by 100 (and 4) then it is only a leap year when it is also divisible by 400. Otherwise it is not.
Test your program with different inputs and make sure it works for them.
For example: -100, 0, 1, 2, 5, 9, 10, 12, 13, 100, blabla
'''

try:
    month = int(raw_input("Please enter a number of moth between 1-12 to show the days: "))
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("This month has 31 days ")

    elif month == 4 or month == 6 or month == 9 or  month == 11:
        print("This month has 30 days")

    elif month == 2:
        leapYear = int(raw_input("Enter a year then we will tell you if feb has 28 or 29 days: "))

        if leapYear % 4 == 0 and leapYear % 100 != 0 or leapYear % 400 == 0:
            print("Leap year 29 days")

        else:
            print("Normal year just 28 days")

    else:
        print("You don't seem to follow rules do you?")


except:
    print("A number you idiot...lol :) ")

try:
    def number_of_days(month):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            print("This month has 31 days ")

        elif month == 4 or month == 6 or month == 9 or  month == 11:
            print("This month has 30 days")

        elif month == 2:
            leapYear = int(raw_input("Enter a year then we will tell you if feb has 28 or 29 days: "))

            if leapYear % 4 == 0 and leapYear % 100 != 0 or leapYear % 400 == 0:
                print("Leap year 29 days")

            else:
                print("Normal year just 28 days")

        else:
            print("You don't seem to follow rules do you?")
except:
    print("oops! try again")

print(number_of_days(13))
