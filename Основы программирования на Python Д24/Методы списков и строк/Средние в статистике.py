from statistics import mean, median
print((lambda li: f'{float(mean(li))} {float(median(li))}')(list(map(float, input().split()))))