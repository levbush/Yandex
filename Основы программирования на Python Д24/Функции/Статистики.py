def print_statistics(arr):
    if arr:
        from statistics import mean, median
        print(len(arr), mean(arr), min(arr), max(arr), median(arr), sep='\n')
    else:
        print('0\n' * 5)