num = int(raw_input("Give me a number: "))

num1 = num%2
num2 = num%4

if num1 == 0:
	print("Even")
else:
	print("Odd")

if num2 == 0:
	print("It is divisable by 4")
else:
	print("Not divisable by 4")