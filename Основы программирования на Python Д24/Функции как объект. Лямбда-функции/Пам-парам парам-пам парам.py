print('Парам пам-пам' if len(set([len(list(filter(lambda x: x in 'аеёиоуыэюя', word))) 
                                  for word in input().split()])) == 1 else 'Пам парам')