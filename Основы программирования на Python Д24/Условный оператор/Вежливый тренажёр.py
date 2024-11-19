print('Назовите себя, пожалуйста!')
name = input()
print('Введите текст.')
s = input()
print('Повторите текст.')
if input() == s:
    print(name + ', введено верно!')
else:
    print(name + ', пока не получилось, попробуйте снова!')