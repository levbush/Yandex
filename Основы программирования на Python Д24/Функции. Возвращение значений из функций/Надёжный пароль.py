def password_level(password: str) -> str:
    if len(password) < 6:
        return 'Недопустимый пароль'
    if password.isdigit() or (password.islower() or password.isupper()) and password.isalpha():
        return 'Ненадежный пароль'
    if (password.islower() or password.isupper()) and not password.isalpha() or password.isalpha():
        return 'Слабый пароль'
    return 'Надежный пароль'