dec, n = int(input()), int(input())
ans = dec
if n == 0:
    print(ans)
else:
    for i in range(n - 1):
        binary = ''    
        while dec > 0:
            binary = str(dec % 2) + binary
            dec //= 2
        binary = str(binary)
        count = binary.count('1')
        bincount = ''
        if count == 0:
            bincount = 0
        else:    
            while count > 0:
                bincount = str(count % 2) + bincount
                count //= 2
        bincount = str(bincount)
        ans = int(binary + bincount, 2)
        dec = ans
print(ans)