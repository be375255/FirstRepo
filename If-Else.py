if __name__ == '__main__':
	n = int(raw_input())

	if n % 2 == 0:
		print("Not Weird")
		even = 1
	else:
		print("Weird")
		odd = 1

	if 2 <= n <= 5:
		if even == 1:
			print("Not Weird")

	if 6 <= n <= 20:
		if even == 1:
			print("Weird")

	if n < 20:
		if even == 1:
			print("NOt Weird")