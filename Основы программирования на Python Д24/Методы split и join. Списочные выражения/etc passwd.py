print(*(lambda users, easy: 
        [f'To: {user[0]}\n{user[4]}, ваш пароль слишком простой, смените его.'
         for user in users if user[1] in easy])
      (list(map(lambda x: ','.join(', '.join(x.split(':')).split(', ')).split(','), 
                iter(input, ''))), input().split(';'), ), sep='\n')