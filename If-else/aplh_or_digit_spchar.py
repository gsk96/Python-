character = input("Enter any character\n")

if 'a' <= character >= 'z':
	print("It is a character")
elif '0' <= character >= '9' :
    print("It is a digit")
else :
    print("It is a special symbol")