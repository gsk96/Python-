month = input("Enter month")

if month == 'January' or month == 'january' or month == 'March' or month == 'march' or month == 'May' or month == 'may' or month == 'July' or month == 'july' or month == 'August' or month == 'October' or month == 'october' or month == 'December' or month == 'december' :
	print(month , "has 31 days")
elif month == 'April' or month == 'april' or month == 'June' or month == 'june' or month == 'September' or month == 'september' or month == 'November' or month == 'november' :
	print(month , "has 30 days")
elif month == 'February' or month == 'february':
	print(month , "has 28days or 29days")
else :
	print("Entered month is invalid")