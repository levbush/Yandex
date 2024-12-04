from collections import defaultdict
rates = defaultdict(int)
for el in list(''.join(input().split()).lower()):
    rates[el] += 1
print(min(list(filter(lambda x: rates[x] == max(rates.values()), rates.keys()))))