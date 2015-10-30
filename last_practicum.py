__author__ = 'Fotty'
from easygui import *

def ask_year():
    year = integerbox("Enter a year: ", lowerbound= 1900, upperbound= 2015)
    message = msgbox( )
    return "You entered" + year
ask_year()