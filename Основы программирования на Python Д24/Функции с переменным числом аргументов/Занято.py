def sequence_occupied(**data):
    arr = []
    for i, new in data.items():
        for el in new:
            places[int(i) - 1][el - 1] = 1 #  type: ignore

    m = r = counter = 0
    for i in range(len(places)): # type: ignore
        for j in places[i]: # type: ignore
            if j == 1:
                counter += 1
            else:
                counter = 0
            if m < counter:
                m, r = counter, i + 1
        counter = 0
    return m, r