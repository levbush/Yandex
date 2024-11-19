x1, y1 = 0, 0
cx, cy = int(input()), int(input())
direction = 1
counter = 0
while x1 != cx or y1 != cy:
	s = input()
	if s == 'налево':
		direction -= 1
		if direction < 1:
			direction += 4
		counter += 1
	elif s == 'направо':
		direction += 1
		if direction > 4:
			direction -= 4
		counter += 1
	elif s == 'разворот':
		direction += 2
		if direction > 4:
			direction -= 4
		counter += 1
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
print(counter)
print('север' if direction == 1 else 'восток' if direction == 2 else 'юг' if direction == 3 else 'запад')