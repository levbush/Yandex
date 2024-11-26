li = [((a := input())[:-2], int(a[-1])) for _ in range(int(input()))]
for i in range(len(li) - 1):
    if li[i][-1] < li[i + 1][-1]:
        print((i + 1, li[i][0]))