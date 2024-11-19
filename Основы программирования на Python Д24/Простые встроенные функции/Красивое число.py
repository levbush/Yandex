n = int(input())
n1, n2, n3 = n // 100, n // 10 % 10, n % 10

nmin = n1 if n1 <= n2 and n1 <= n3 else n2 if n2 <= n1 and n2 <= n3 else n3
nmax = n1 if n1 >= n2 and n1 >= n3 else n2 if n2 >= n1 and n2 >= n3 else n3
nmid = n1 if (n2 == nmin or n2 == nmax) and (n3 == nmin or n3 == nmax) else ''
if nmid == '':
    nmid = n2 if (n1 == nmin or n1 == nmax) and (n3 == nmin or n3 == nmax) else n3
                                                            
print('Вы ввели красивое число' if (nmin + nmax) / 2 == float(nmid) else 'Жаль, вы ввели обычное число')