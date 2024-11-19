listt = [0, 0, 1]


def tribonacci(n):
    if len(listt) >= n + 1:
        return listt[n]
    listt.append(sum(listt[-3:]))
    return tribonacci(n)

