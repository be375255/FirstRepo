n = int(raw_input())
even = false
odd = false

if n % 2 == 0:
	print("Not Weird")
	even = true
else:
	print("Weird")
	odd = true

if 2 <= n <= 5:
	if even == true:
		print("Not Weird")

#f 6 <= n <= 20:
#	if even == 1:
#		print("Weird")

#if n < 20:
#	if even == 1:
#		print("NOt Weird")