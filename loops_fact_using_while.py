fact = 1
i = 1
number = int(input("Enter number to find factorial:"))
while(i<=number):
	fact = fact * i;
	i = i+1
print("The factorial is of",number, "is",fact)