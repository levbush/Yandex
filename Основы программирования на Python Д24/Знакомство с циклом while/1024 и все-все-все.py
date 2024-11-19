n = int(input())
counter = 0
flag = False
if n == 1:
	print(0)
else:
	while n >= 2:
		counter += 1
		if n == 2:
			flag = True
		n /= 2
	print(counter if flag else 'НЕТ')
