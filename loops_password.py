password = "key123"
for i in range(3):
	passwd = input("Enter password")
	chances = 2
	if(passwd == password):
		print("Welcome")
		break
	else:
		print("Wrong password,chances left",chances-i)
		continue
print("You have failed , Try again later")