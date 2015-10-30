from easygui import *
from turtle import *

'''
Home Exercise 1: Flag
Choose one country's flag (with at least three colors or with more complex shape)
(http://www.flags.net/) and draw it with turtle.
'''





'''
Home Exercise 2: Asking input with GUI
Make a program that asks the user for his/her name and his/her birth month number and then shows message
that includes both the name of the user and the number of days in the entered month
(for example "John's birth month has 31 days").
 All information must be asked and shown with EasyGUI.
 To calculate the number of days in a month, use the function you have written in previous homework.
'''


mychoices = ["my favorite","easy","ok","difficult"]
pressed = choicebox("Programming is ", choices = mychoices)
if pressed == None:
    msgbox("You did not choose anything, you little rebel!")
elif pressed == "my favorite":
    msgbox("Programming is your favorite course! As it should be!")
else:
    msgbox("So you think that programming is " + pressed + ", hmm, interesting!")