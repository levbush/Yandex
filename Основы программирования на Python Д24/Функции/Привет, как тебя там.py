def who_are_you_and_hello():
    while True:
        if not (inp := input()).isalpha() or inp != inp.capitalize():
            continue
        print(f'Привет, {inp}!')
        break