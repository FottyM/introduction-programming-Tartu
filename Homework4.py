from pip.backwardcompat import raw_input

__author__ = 'Fotty'

"""
Write a program that prompts a user for their name (first name and family name separately) and then welcomes them.
This time, the program should always welcome so that both the first name and the last name begin with a capital letter
and the rest of the letters are small, regardless of how the name was entered (only in small letters, in large or mixed).
Program should compute initials from entered full name and display them.
Also a program should find and print out the number of vowels (letters A, E, I, O, U)
in the name (in both, first and family, names).
 Enter first name: mAriNa
 Enter family name: lePp
 Hello Marina Lepp
 Your initials are M L
 The number of vowels in your name is 4

"""
first_name = str(raw_input("Enter you name: "))
last_name = str(raw_input("Enter your last name: "))
rearrange_words = first_name.lower().capitalize() + " " + last_name.lower().capitalize()
initials = first_name[0].upper() + last_name[0].upper()
vowels = "aeiouAEIUO"
summ = 0

for v in vowels:
    v = rearrange_words.count(v)
    summ += v
print("Hello {0}\nYour initials are {1}\nThe number of vowels in your name is {2}".format(rearrange_words, initials,
                                                                                          str(summ)))

"""
Every University of Tartu user (student or member of staff), which has username for Study Information System,
has home directory and can create webpage using university server.
The url for his/her webpage would be www.ut.ee/~username/ (for example, www.ut.ee/~vilo/).
Write a program that prompts a user for university url, finds and prints out the username.
Here is an example of program output.

 Please enter url: http://www.ut.ee/~koit/KT/index_eng.html
 Username is koit
"""
address = raw_input("Please enter url: ")

fpos = address.find("~")
lpos = address.find("/", fpos)

username = address[fpos + 1:lpos]

print("Username is", username)