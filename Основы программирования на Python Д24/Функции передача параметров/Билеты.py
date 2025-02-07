def allocation(data):
    arr = []
    for i, j in data:
        if not places[i - 1][j - 1]:  # type: ignore
            places[i - 1][j - 1] = 1  # type: ignore
        else:
            arr.append((i, j))
    return arr