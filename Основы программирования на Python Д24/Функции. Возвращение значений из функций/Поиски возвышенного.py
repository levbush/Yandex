def find_mountain(heightsMap: list) -> tuple:
    m = ans = 0
    for i in range(len(heightsMap)):
        for j in range(len(heightsMap[i])):
            if heightsMap[i][j] > m:
                m = heightsMap[i][j]
                ans = i, j
    return ans