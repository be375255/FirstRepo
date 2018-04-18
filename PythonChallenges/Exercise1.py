name = raw_input("What is your name: ")

print("Your name is " + name)

age = int(raw_input("What is your age: "))

print("Your age is " + str(age))

if age > 0:
	age = 100 - age

print("You will be 100 in " + str(age) + " years!")