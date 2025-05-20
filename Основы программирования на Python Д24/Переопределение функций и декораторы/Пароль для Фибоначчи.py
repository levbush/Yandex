def check_password(old_func):
    def new_func(*args, **kwargs):
        if input() != '123':
            print('В доступе отказано')
            return
        return old_func(*args, **kwargs)
    return new_func


@check_password
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)