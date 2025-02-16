def partial_sums(*data):
    return [0 + sum(data[:i]) for i in range(len(data) + 1)]