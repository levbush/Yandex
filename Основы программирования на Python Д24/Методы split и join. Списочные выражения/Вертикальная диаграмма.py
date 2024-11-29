print((lambda li: '\n'.join(['*' * (len(li) + 2) if i == max(li) + 2
                             else '*' + ''.join(['*' if i <= el 
                                                 else ' ' for el in li]) 
                             + '*' for i in range(max(li) + 2, 0, -1)]))
      (list(map(int, input().split()))))