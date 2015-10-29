__author__ = 'Fotty'
a = [2,3,1,5]
b = [6,4]
c = a+b
#c.sort()
print(c)

def name_as_month(mon):
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return month[mon-1]

print(name_as_month(11))

def date(st):
    month = st[3:5]
    return (name_as_month(month),",",)

xcel = open("python.csv")

for line in xcel:
    separator = line.split(",")
    line.strip()
    print("First name: " + separator[0])
    print("Last name: "+ separator[1])
    print("ID: " + separator[2])
    print("---------------------------")


