__author__ = 'Fortunat Mutunda'
from pip._vendor.distlib.compat import raw_input

'''
Exercise 1. Number of days in months

Rewrite the number of days in months program from the previous week using a function called number_of_days
that takes a number of the month as its parameter and returns the number of days in that month.

Run the program repeatedly to test the various different values for input.
'''


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
        return ("You don't seem to follow rules do you?")


try:
    print (number_of_days(int(raw_input("Please enter the month you wanna check=> "))))
except:
    print('A number please ')

"""
Exercise 2. ECTS and hours

Write a function called hours_per_week that takes two parameters:
 the number of ETCS (EAP in Estonian) and the number of weeks the course is running and returns the number of hours
 per week which student should spend on this course. (1 EAP is 26 hours).
 You can reuse and modify your solution from the first week (if you have participated the practicum).

"""

def hours_per_week(credit, total_weeks):
    total_hours = 26 * credit
    weekly_hours = total_hours / total_weeks
    return "You are going to spend this much " + str(weekly_hours) + " hours per week"


print(hours_per_week(6, 16))
