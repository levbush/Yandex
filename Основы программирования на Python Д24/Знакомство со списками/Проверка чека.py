n, checksum = list(map(int, input().split()))

check = [list(input()) for _ in range(n)]
for i in range(n):
    check[i] = [int(''.join(check[i][:7])), int(''.join(check[i][8:12])), int(''.join(check[i][13:]))]
wrongs = [i + 1 for i in range(len(check)) if check[i][0] * check[i][1] != check[i][2]]
for i in wrongs:
    i -= 1
    check[i][-1] = check[i][0] * check[i][1]
real_check_sum = sum([i[-1] for i in check])
print(checksum - real_check_sum)
print(*wrongs)