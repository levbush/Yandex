def print_average(arr):
    from statistics import mean
    print(float(mean(arr)) if arr else 0)