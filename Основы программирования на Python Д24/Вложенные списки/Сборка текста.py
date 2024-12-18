indexes = list(map(int, input().split()))
string = input().split()
ans = []
for i in indexes:
    ans.append(string[i - 1])
print(' '.join(ans).capitalize())