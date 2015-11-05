__author__ = 'Fotty'

first_name = raw_input("Name: ")
last_name = raw_input("Last name: ")
names = str(first_name + " " + last_name)
date_of_birth = raw_input("Date of birth: ")
date_of_death = raw_input("Dead : ")
dates = str(date_of_death + "-" + date_of_birth)
size = max(len(names), len(dates)) + 10
print("+" + "-" * size + "+")
print("|" + " " * size + "|")
print("|" + names.center(size) + "|")
print("|" + " " * size + "|")
print("|" + dates.center(size) + "|")
print("|" + " " * size + "|")
print("+" + "-" * size + "+")

word = raw_input()
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









