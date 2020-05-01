
def count_upper_lower():
	strng = input("Please enter a String without spaces : ")
	Uppercase = 0
	Lowercase = 0
	if strng.isalpha() :
		for letter in strng:
			if letter.isupper():
				Uppercase = Uppercase + 1
			else:
				Lowercase = Lowercase + 1
	else:
		print("Invalid String")
		#break
	print("Uppercase :",Uppercase)
	print("Lowercase :",Lowercase)

count_upper_lower()