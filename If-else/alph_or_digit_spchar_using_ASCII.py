ASCII_number = input("Enter any ASCII\n")

if ASCII_number >= '97' and ASCII_number <= '122' or ASCII_number >= '65' and ASCII_number <= '90':
	print("It is a character")
elif ASCII_number >= '48' and ASCII_number<='57':
    print("It is a digit")
else :
    print("It is a special symbol")