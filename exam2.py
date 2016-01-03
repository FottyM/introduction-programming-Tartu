# Will try with a list
attending_guests = 0
not_sure_if_attending_guests = 0


def budget(number_of_people):
    room = 100
    food = 15
    min_budget = room + food * (number_of_people - not_sure_if_attending_guests)
    max_budget = room + (number_of_people * food)
    return "Minimum budget is: " + str(min_budget) + " EUR" + "\n" + "Maximum budget is: " + str(max_budget) + " EUR"


try:
    guestsFile = open('guests.txt')
    guest_list = []
    for line in guestsFile:
        guest = line.strip()
        guest_list = guest_list.append(guest)

        if "+" in guest:
            attending_guests += 1
            print(guest[2:] + " is attending ")

        elif "?" in guest:
            not_sure_if_attending_guests += 1
            print(guest[2:] + " doesn't know yet ")
    print(guest_list)
    print("Number of people attending: " + str(attending_guests))
    print("Number of people who don't know yet: " + str(not_sure_if_attending_guests))
    num_of_ppl = attending_guests + not_sure_if_attending_guests
    total = budget(num_of_ppl)
    print(total)

except:
    print("File doesn't exist")
