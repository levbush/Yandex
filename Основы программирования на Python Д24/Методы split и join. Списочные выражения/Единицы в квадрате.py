print(', '.join((lambda num: [str(i ** 2) for i in [int('1' * j) for j in range(1, len(num) + 1) 
                                                    if int('1' * j) <= int(num)]])(input())))