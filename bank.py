__author__ = 'Fotty'
import random
<<<<<<< HEAD
<<<<<<< HEAD
from pip._vendor.distlib.compat import raw_input
=======
# from pip._vendor.distlib.compat import raw_input
>>>>>>> beb7af1... Will do this later but I have to start
=======
# This is the finale project I made
# works with Python 2

>>>>>>> second

'''
1. Create your own account

2. Deposit money

3. Withdraw money

4. Check money in your account balance

5. Change password account
'''


account = open('data.txt', 'a')

def to_string(string):
    if (len(string) < 10):

        for i in range(len(string), 10, 1):
            string = "0" + string
    return string


def create_account():
    account = open('data.txt', 'a')
    first_name = raw_input("first name: ")
    last_name = raw_input("last name: ")
    password = "0000"
    balance = 0
    account_number = to_string(str(random.randint(0, 10000000000) % 10000000000))
    acc_details = first_name + "," + last_name + "," + str(password) + "," + str(balance) + "," + str(
        account_number) + "\n"
    account.write(acc_details)
<<<<<<< HEAD
<<<<<<< HEAD
    print("Done! ")
=======
    print "Done! "
    print(
        "Your password is 0000 and your account number is " + account_number + "\nplease make sure you change your password imediatly: ")
>>>>>>> beb7af1... Will do this later but I have to start
=======
    print "Done! "
    print(
        "Your password is 0000 and your account number is " + account_number + "\nplease make sure you change your password imediatly: ")
>>>>>>> second


def deposit_money():
    account = open('data.txt', 'r+')
    first_name = raw_input("What's your name please: ")
    password = str(raw_input("Password please: "))
    lines = account.readlines()
    bigIndex = -1

    for index in range(len(lines)):
        dets = (lines[index].split(","))

        if (dets[0] == first_name) and (dets[2] == password):
<<<<<<< HEAD
            money_to_deposit = raw_input("Enter the amount of money to deposit ")
            sum = str(float(dets[3]) + float(money_to_deposit))
            #print(sum)

            dets[3] = str(sum)
            print(dets[3], dets)
            bigIndex = index
            break
=======
            money_to_deposit = float(raw_input("Enter the amount of money to deposit: "))
            if 0.0 < money_to_deposit:
                sum = str(float(dets[3]) + float(money_to_deposit))
                dets[3] = str(sum)
                bigIndex = index
                print "Your balance is now: " + dets[3]
                break
            else:
                print("Is that money? please try again ")
>>>>>>> second

    if (bigIndex != -1):
        lines[bigIndex] = (",".join(el for el in dets))
    account.close()

    account = open('data.txt', 'w+')
    for element in lines:
        account.write(element)
<<<<<<< HEAD
<<<<<<< HEAD
    print(dets)
    return "Money deposited: ", dets[3]

=======

        #return "Money deposited: " + dets[3]
>>>>>>> beb7af1... Will do this later but I have to start
=======

        #return "Money deposited: " + dets[3]
>>>>>>> second


def withdraw_money():
    account = open('data.txt', 'r+')
    first_name = raw_input("What's your name please: ")
    password = raw_input("Password please: ")
    lines = account.readlines()
    bigIndex = -1

    for index in range(len(lines)):
        dets = (lines[index].split(","))

        if (dets[0] == first_name) and (dets[2] == password):
            money_to_withdraw = raw_input("How much do you want to withdraw: ")

<<<<<<< HEAD
<<<<<<< HEAD
            dets[3] = str(sum)
            print(dets[3], dets)
            bigIndex = index
            break
=======
=======
            if float(money_to_withdraw) > 0 and float(money_to_withdraw) <= float(dets[3]):

>>>>>>> second
                sum = str(float(dets[3]) - float(money_to_withdraw))
                dets[3] = str(sum)
                print dets[3] + "Withdrawn "
                bigIndex = index

            else:
                print "Not enough money into your account"
                #else:
                #   print "Wrong credentials please try again: "
<<<<<<< HEAD
>>>>>>> beb7af1... Will do this later but I have to start
=======
>>>>>>> second

    if (bigIndex != -1):
        lines[bigIndex] = (",".join(el for el in dets))
    account.close()

    account = open('data.txt', 'w+')
    for element in lines:
        account.write(element)

    return "Withdrawn " + dets[3]

def check_account():
    account = open('data.txt', 'r+')
    first_name = raw_input("What's your first name please: ")
    password = raw_input("Password please: ")
    lines = account.readlines()

    for index in range(len(lines)):
        dets = (lines[index].split(","))

        if (dets[0] == first_name) and (dets[2] == password):
<<<<<<< HEAD
<<<<<<< HEAD
            print("First name and last name ", dets[0], dets[1])
            print("Account Number: ", dets[4].strip())
            print("Balance: ", dets[3].strip())
=======
            print "First name and last name: " + dets[0] + " " + dets[1]
            print "Account Number: " + dets[4].strip()
            print "Balance: " + dets[3].strip()
>>>>>>> beb7af1... Will do this later but I have to start
=======
            print "First name and last name: " + dets[0] + " " + dets[1]
            print "Account Number: " + dets[4].strip()
            print "Balance: " + dets[3].strip()
>>>>>>> second
            break


def change_password():
    account = open('data.txt', 'r+')
    first_name = raw_input("What's your name please: ")
    password = str(raw_input("Enter old password please: "))
    lines = account.readlines()
    bigIndex = -1

    for index in range(len(lines)):
        dets = (lines[index].split(","))

        if (dets[0] == first_name) and (dets[2] == password):
<<<<<<< HEAD
<<<<<<< HEAD
            enter_new_password = int(raw_input("Enter new password:\n "))
            new_password = str(enter_new_password)
            dets[2] = str(new_password)
            bigIndex = index
            break
=======
=======
>>>>>>> second
            enter_new_password = int(raw_input("Enter new password: "))
            if (len(str(enter_new_password)) == 4):
                new_password = enter_new_password
                dets[2] = str(new_password)
                bigIndex = index
                print("Password updated! \n")
                break
            else:
                print("4 digits please: ")
        else:
            print("Something went wrong :X")
<<<<<<< HEAD
>>>>>>> beb7af1... Will do this later but I have to start
=======
>>>>>>> second

    if (bigIndex != -1):
        lines[bigIndex] = (",".join(el for el in dets))
    account.close()

    account = open('data.txt', 'w+')
    for element in lines:
        account.write(element)
<<<<<<< HEAD
<<<<<<< HEAD
    return "Password updated\n "

=======
        #return "Password updated\n "
>>>>>>> beb7af1... Will do this later but I have to start
=======
        #return "Password updated\n "
>>>>>>> second


while True:

    print("\nPress 1 2 3 4 5 or type exit to quit:\n"
<<<<<<< HEAD
<<<<<<< HEAD
              "1.To create an account:\n"
              "2.To make a deposit: \n"
              "3.To withdraw money\n"
              "4.To Check the balance:\n"
              "5.Change password: \n")
=======
=======
>>>>>>> second
          "1.To create an account:\n"
          "2.To make a deposit: \n"
          "3.To withdraw money\n"
          "4.To Check the balance:\n"
          "5.Change password: ")
    choice = str(raw_input())
<<<<<<< HEAD
>>>>>>> beb7af1... Will do this later but I have to start
=======
>>>>>>> second
    try:
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_account()
        elif choice == '5':
            change_password()
        elif choice == 'exit':
            break
    except:
        print("Exception ")



#God bless
