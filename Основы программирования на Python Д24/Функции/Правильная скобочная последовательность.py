def bracket_check(test_string: str) -> None:
    stack = []
    for symbol in test_string:
        if symbol == '(':
            stack.append('(')
        elif symbol == ')':
            try:
                stack.pop()
            except IndexError:
                print('NO')
                return
    print('NO' if stack else 'YES')