__author__ = 'Fotty'
"""
Exercise 1. Celsius and Fahrenheit

Rewrite Celsius-Fahrenheit program from previous week which reads temperatures from file to store the converted
temperatures into a list. The program should print out the average, maximum and minimum of the temperatures.
"""

xfile = open("temperatures.txt", 'r')
tempList = []
acc = 0
for temp in xfile:
    try:
        c = str(temp.strip())
        f = (float(temp.strip()) * 9/5 + 32)
        acc += float(f)
        tempList.append(f)
    except:
        print("Invalid input")
print(tempList)
print("The average is ", str(acc/len(tempList)))
print("Max temp is ", max(tempList), "and the min temperature is", min(tempList))



"""
Exercise 2. Number of days in months
Rewrite the number of days in months program from week 4 so that the program would read dates in form dd.mm.yyyy
from file that looks like this (ask filename from user),
pick up the number of month from each line and print out the number of days in this month.
Rewrite your function that it would not contain conditional (if) statements for getting the number of days.
Your function should do it using a list.
Do not check for leap year (let’s say that number of days in february is always 28).
"""


fsx = raw_input("Name of the file to read please: ")
file_content = open(fsx)

def number_of_days(content):
    output = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 31, 30]
    return str(output[content-1])

for line in file_content:
    number_of_days(int(line[3:5]))