number_1 = int(input("Enter 1st number\n"))
number_2 = int(input("Enter 2nd number\n"))
number_3 = int(input("Enter 3rd number\n"))

if number_1 > number_2 and number_1 > number_3:
	print("Maximum number is:",number_1)
elif number_2 > number_1 and number_2 > number_3:
	print("Maximum number is:",number_2)
else:
	print("Maximum number is:",number_3)