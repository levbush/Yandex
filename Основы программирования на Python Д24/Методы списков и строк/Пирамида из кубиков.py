for _ in range(int(input())):
    queue = list(map(int, input().split()))
    flag = True
    ans = []
    lastcube = float('inf')
    while queue:
        cube1, cube2 = queue[0], queue[-1]
        if cube1 > lastcube and cube2 > lastcube:
            flag = False
            break
        else:
            if cube2 < cube1 <= lastcube:
                cube = cube1
                queue.pop(0)
            elif cube2 <= lastcube:
                cube = cube2
                queue.pop()
            else:
                flag = False
                break
        ans.append(cube)
        lastcube = cube
    if flag:
        print(*ans)
    else:
        print('НЕТ')
