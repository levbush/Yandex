while True:
	password = input()
	p2 = input()
	if len(password) < 8:
		print('Короткий!')
	elif '123' in password:
		print('Простой!')
	elif p2 != password:
		print('Различаются.')
	else:
		print('OK')
		break