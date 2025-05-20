def check_password(password):
    def decorator(old_func):
        def new_func(*args, **kwargs):
            nonlocal password
            passw = password
            if input() != passw:
                print('В доступе отказано')
                return
            return old_func(*args, **kwargs)
        return new_func
    return decorator