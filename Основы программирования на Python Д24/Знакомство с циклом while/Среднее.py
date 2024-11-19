s = float(input())
counter = 0
ssum = 0
while s >= -300:
	counter += 1
	ssum += s
	s = float(input())
print(ssum / counter)