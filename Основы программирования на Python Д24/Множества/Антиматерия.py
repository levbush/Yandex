from functools import reduce
s = ''
inp = input()
while inp:
    s += inp + ' '
    inp = input()
s = s.split('-1')
for i in range(len(s)):
    s[i] = s[i].strip().split()

for i in range(len(s)):
    s[i] = set(s[i])
    s[i] = list(s[i])
s = reduce(list.__add__, [i for i in s])
print(*set(s) - {i for i in s if s.count(i) > 1})