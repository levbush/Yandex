x1, y1 = 0, 0
cx, cy = int(input()), int(input())
direction = 1
counter = 0
s = ''
while 'стоп' not in str(s):
	s = input()
	if s == 'север':
		direction = 1
	elif s == 'юг':
		direction = 3
	elif s == 'запад':
		direction = 4
	elif s == 'восток':
		direction = 2
	elif s.isdigit():
		s = int(s)
		if direction == 1:
			y1 += s
		elif direction == 2:
			x1 += s
		elif direction == 3:
			y1 -= s
		elif direction == 4:
			x1 -= s
		counter += 1
	if x1 == cx and y1 == cy:
		break
print(counter)