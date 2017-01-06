from random import randint

car = randint(1,3)
user_door = int(raw_input("Pick either door 1, 2, or 3: "))

if user_door == 1:
	switch1 = 2
	switch2 = 3
elif user_door == 2:
	switch1 = 1
	switch2 = 3
else:
	switch1 = 1
	switch2 = 2

if car == 1:
	goat1 = 2
	goat2 = 3
elif car == 2:
	goat1 = 1
	goat2 = 3
else:
	goat1 = 1
	goat2 = 2

reveal = goat1
switch = switch2

if goat1 == user_door:
	reveal = goat2
if switch2 == reveal:
	switch = switch1

print "\nOk...but I want to tell you something:"
print "behind door number %d...is a goat." % reveal

answer = raw_input("\nDo you want to change your pick to door number %d? (type yes or no): " % switch)

def change_answer(yes_no, switch, user_door):
	if yes_no == "yes":
		user_door = switch
		return user_door
	elif yes_no == "no":
		return user_door
	else:
		change_answer(answer, switch, user_door)

user_door = change_answer(answer, switch, user_door)


if user_door == car:
	print "\nCongradulations! You've won yourself a brand new car! (in spirit)"
if user_door != car:
	print "\nYikes, that's a goat."