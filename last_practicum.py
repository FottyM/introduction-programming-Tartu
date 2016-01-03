__author__ = 'Fotty'
<<<<<<< HEAD
from easygui import *

def ask_year():
    year = integerbox("Enter a year: ", lowerbound= 1900, upperbound= 2015)
    message = msgbox( )
    return "You entered" + year
ask_year()
=======

# (format is: month;year;salary;money spent):
fileX = open("details.txt")

save_money = []
overdue_money = []
beneficial_months = 0
useless_months = 0


def ask_year():
    index = 0
    bnfm = 0
    ulm = 0

    year = int(raw_input("Enter a year between 1900 and 2015 please: "))
    if 1900 <= year < 2016:

        for line in fileX:

            records = line.strip().split(";")

            if str(year) == records[1]:
                # print(list[1])
                index += 1
                savings = float(records[2]) - float(records[3])
                if savings == 0:
                    print("In " + records[0] + " " + records[1] + " you spent all money you earned.")
                elif savings > 0:
                    save_money.append(savings)
                    bnfm += 1
                    beneficial_months = beneficial_months + bnfm
                    print("In " + records[0] + " " + records[1] + " you saved " + str(savings))

                else:
                    overdue_money.append(-savings)
                    ulm += 1
                    str(useless_months) = str(useless_months) + str(ulm)
                    print("In " + records[0] + " " + records[1] + " you were over the budget " + str(-savings))

        print("We found information about " + str(index) + " months.")


    else:
        print("hmmmm")


def total_savings(saved, lost):
    total = saved - lost
    return str(total)


# noinspection PyBroadException
try:
    ask_year()
    s = sum(save_money)
    l = sum(overdue_money)
    balance = (str(total_savings(s, l)))
    print("You saved a total of " + balance)
    print(max(save_money))
    print(str(beneficial_months))

    print(max(overdue_money))
    print(str(useless_months))
except:
    print('oops')
>>>>>>> second
