print("Enter DIFFERENT numbers")
numbers = []

while True:
	try:
		num = int(input('>>> '))
	except:
		exit()

	numbers.append(num)
	numbers.sort(reverse=True)

	if 2 in set([numbers.count(numb) for numb in numbers]):
		numbers.remove(num)
		print("Duplicate Detected!")

	print(numbers)
