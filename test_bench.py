#from pip._vendor.distlib.compat import raw_input

__author__ = 'Fotty'

# Triangle
# Intergers not divisible by 10
# Clecius Farheneit

first_name = input("Name: ")
last_name = input("Last name: ")
names = str(first_name + " " + last_name)
date_of_birth = input("Date of birth: ")
date_of_death = input("Dead : ")
dates = str(date_of_death + "-" + date_of_birth)
size = max(len(names), len(dates)) + 10
print("+" + "-" * size + "+")
print("|" + " " * size + "|")
print("|" + names.center(size) + "|")
print("|" + " " * size + "|")
print("|" + dates.center(size) + "|")
print("|" + " " * size + "|")
print("+" + "-" * size + "+")





word = input()
n = len(word)/2

for i in raw_input(n):
    if word[i] != word[len(word)-1 -i]:
        print("duh")
        break
    elif word[i] == word[len(word)-1-i] and i == n-1:
        print("Hmmmmm")

var = 0
filehandler = open("data.txt")
for line in filehandler:
    if "programming" in line:
        var += 1
        print(var)

        print(line)

username = "Mo\nty"
password = "Py\thon"

print("Username is " + username)
print("Password is " + password)









