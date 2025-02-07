data = list(map(int, input().split()))
ans = []
for n in data:
    bin_n = bin(n)[2:]
    ans.append({'digits': len(bin_n), 'units': bin_n.count('1'), 'zeros': bin_n.count('0')})
print(ans)