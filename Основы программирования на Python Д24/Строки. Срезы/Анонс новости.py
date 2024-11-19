max_len = int(input())
for _ in range(int(input())):
    if len(i := input()) > max_len:
        i = i[:max_len - 3] + '...'
    print(i)