number1 = 0

for number1 in range (1,100):
	if number1%3 == 0 and number1%5 != 0:
		print("bum")
	elif number1%5 == 0 and number1%3 != 0: 
		print("bác")
	elif number1%3 == 0 and number1%5 == 0:
		print("bum-bác")
	else:
		print(0+number1)








