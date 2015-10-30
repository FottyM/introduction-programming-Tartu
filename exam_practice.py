__author__ = 'Fotty'

'''
Write a program that reads a file that contains values of euro cents in each row and finds the sum (total amount)
of euro cents and the value of smallest red coin (red coins are with values 1, 2 and 5).
Cents are in the file cents.txt, where each line represents a coin (make the file by yourself).
Find the sum of euro cents (valid euro coins are 1, 2, 5, 10, 20 and 50) and sum of unknown cents (the remaining numbers).
Find the value of smallest red coin (1, 2, 5) or report about their absence.
'''
try:
    filehandler = open("cents.txt")
except:
    print("oops")
    exit()

cents = []

for line in filehandler:
    cents.append(int(line))
    print(cents)