def gen_spam_email(email: str, name: str, data: str, place: str = 'Москва') -> str:
    return f'''To: {email}
Здравствуйте, {name}!
Были бы рады видеть вас на встрече начинающих программистов в {place}, которая пройдет {data}.'''


print(gen_spam_email(email='some.email@gmail.com', name='Name', data='10.02.2025'))
print(gen_spam_email(email='some-other-email@gmail.com', name='Another Name', data='10.02.2030', place='Moon'))