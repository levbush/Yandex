li = [input() for _ in range(int(input()))]
for i in range(len(li)):
    if 'кот' in li[i]:
        print(i + 1, li[i].index('кот') + 1)
