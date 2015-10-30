from easygui import *
from turtle import *
'''
Home Exercise 1: Flag
Choose one country's flag (with at least three colors or with more complex shape)
(http://www.flags.net/) and draw it with turtle.
'''
setup(600,400)
title("swiss flag")
speed(10)
penup()
right(90)
forward(100)
left(90)
pendown()
color("white")
bgcolor('red')
begin_fill()
forward(20)
left(90)
forward(60)
right(90)
forward(60)
left(90)
forward(20)
left(90)
forward(60)
right(90)
forward(60)
left(90)
forward(20)
left(90)
forward(60)
right(90)
forward(60)
left(90)
forward(20)
left(90)
forward(60)
right(90)
forward(60)
end_fill()
exitonclick()



'''
Home Exercise 2: Asking input with GUI
Make a program that asks the user for his/her name and his/her birth month number and then shows message
that includes both the name of the user and the number of days in the entered month
(for example "John's birth month has 31 days").
 All information must be asked and shown with EasyGUI.
 To calculate the number of days in a month, use the function you have written in previous homework.
'''


def ask_year():
    name = enterbox("Hi what's your name?")
    birth_month = integerbox("What is your birth month? ", lowerbound = 1, upperbound = 12)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 31, 30]

    if name == None or birth_month == None or name == "":
        msgbox("Why do you have rebel, enter things like a normal human!!")
    else:
        for i in range(len(days_in_month)):
            if i != birth_month:
                continue
            else:
                msgbox(str(name) + " 's birth month has " + str(days_in_month[i-1])+" days")
                break

ask_year()