s = input()
li = ['', '', '', '', '']
for j in range(len(s)):
    li[0] += '** ' if s[j] == 'B' else ' * '
    li[0] += '  '
for j in range(len(s)):
    li[1] += '* *'
    li[1] += '  '
for j in range(len(s)):
    li[2] += '***' if s[j] == 'A' else '** ' if s[j] == 'B' else '*  '
    li[2] += '  '
for j in range(len(s)):
    li[3] += '* *'
    li[3] += '  '
for j in range(len(s)):
    li[4] += '* *' if s[j] == 'A' else '** ' if s[j] == 'B' else ' * '
    li[4] += '  '
print(*li, sep='\n')