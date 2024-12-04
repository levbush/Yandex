from statistics import median, mode
print((lambda li: f'{int(median(li))} {int(mode(li))}')(list(map(float, input().split()))))