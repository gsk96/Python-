n = int(input())
a = []
while n>0:
	remainder = n%2
	a.append(remainder)
	n = n // 2
a.reverse()
print(a)