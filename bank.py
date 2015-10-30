__author__ = 'Fotty'
import random
#from pip._vendor.distlib.compat import raw_input

'''
1. Create your own account

2. Deposit money

3. Withdraw money

4. Check money in your account balance

5. Change password account
'''


#account = open('data.txt', 'a')

def to_string(string):
    if( len(string) < 10 ):
        for i in range(len(string),10,1):
            string = "0" + string
    return string

def create_account():
    account = open('data.txt', 'a')
    first_name = raw_input("first name: ")
    last_name = raw_input("last name: ")
    password = raw_input("password 4 digits: ")
    balance = 0
    account_number = to_string(str(random.randint(0,10000000000) % 10000000000))
    acc_details = first_name + ","+last_name+","+str(password)+","+str(balance)+","+str(account_number) + "\n"
    account.write(acc_details)
    print "Done! "


def deposit_money():
    account = open('data.txt', 'r+')
    first_name = raw_input("What's your name please: ")
    password = str(raw_input("Password please: "))
    lines = account.readlines()
    bigIndex = -1

    for index in range(len(lines)):
        dets = (lines[index].split(","))

        if (dets[0] == first_name) and (dets[2] == password):
            money_to_deposit = raw_input("Enter the amount of money to deposit: ")
            sum = str(float(dets[3]) + float(money_to_deposit))
            dets[3] = str(sum)
            bigIndex = index
            break

    if(bigIndex != -1):
        lines[bigIndex] = (",".join(el for el in dets))
    account.close()

    account = open('data.txt', 'w+')
    for element in lines:
        account.write(element)
    print "Your balance is now: " + dets[3]
    return "Money deposited: " + dets[3]



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

            if float(money_to_withdraw) > 0 and float(money_to_withdraw) <= float(dets[3]):

                sum = str(float(dets[3]) - float(money_to_withdraw))
                dets[3] = str(sum)
                print dets[3] + "Withdrawn "
                bigIndex = index

            else:
                print "Not enough money into your account"
        #else:
         #   print "Wrong credentials please try again: "

    if(bigIndex != -1):
        lines[bigIndex] = (",".join(el for el in dets))
    account.close()

    account = open('data.txt', 'w+')
    for element in lines:
        account.write(element)

    return "Money deposited: " + dets[3]



def check_account():
    account = open('data.txt', 'r+')
    first_name = raw_input("What's your first name please: ")
    password = raw_input("Password please: ")
    lines = account.readlines()

    for index in range(len(lines)):
        dets = (lines[index].split(","))

        if (dets[0] == first_name) and (dets[2] == password):
            print "First name and last name: " + dets[0]+ " " + dets[1]
            print "Account Number: " + dets[4].strip()
            print "Balance: " + dets[3].strip()
            break


def change_password():
    account = open('data.txt', 'r+')
    first_name = raw_input("What's your name please: ")
    password = str(raw_input("Password please: "))
    lines = account.readlines()
    bigIndex = -1

    for index in range(len(lines)):
        dets = (lines[index].split(","))

        if (dets[0] == first_name) and (dets[2] == password):
            enter_new_password = int(raw_input("Enter new password:\n "))
            new_password = str(enter_new_password)
            dets[2] = str(new_password)
            bigIndex = index
            break

    if(bigIndex != -1):
        lines[bigIndex] = (",".join(el for el in dets))
    account.close()

    account = open('data.txt', 'w+')
    for element in lines:
        account.write(element)
    return "Password updated\n "



while True:

    print("\nPress 1 2 3 4 5 or type exit to quit:\n"
              "1.To create an account:\n"
              "2.To make a deposit: \n"
              "3.To withdraw money\n"
              "4.To Check the balance:\n"
              "5.Change password: \n")
    choice = str(raw_input())
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




