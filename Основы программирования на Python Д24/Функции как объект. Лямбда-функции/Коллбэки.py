def ask_password(login, password, success=lambda x: None, failure=lambda x, y: None):
    flag1, flag2 = len(list(filter(lambda x: x in 'aeiouy', password.lower()))) == 3, list(
        filter(lambda x: x not in 'aeiouy', password.lower())) == list(
        filter(lambda x: x not in 'aeiouy', login.lower()))
    failure(login.lower(),
            'Everything is wrong' if not flag1 and not flag2 else 'Wrong number of vowels' if not flag1
            else 'Wrong consonants') if not flag1 or not flag2 else success(
        login)
    return (
        'Everything is wrong' if not flag1 and not flag2 else 'Wrong number of vowels' if not flag1
        else 'Wrong consonants') if not flag1 or not flag2 else True


def main(login, password):
    if (err := str(ask_password(login, password))) == 'True':
        print(f'Привет, {login.lower()}!')
    else:
        print(f'Кто-то пытался притвориться пользователем {login.lower()}, но в пароле допустил ошибку: {err.upper()}.')
