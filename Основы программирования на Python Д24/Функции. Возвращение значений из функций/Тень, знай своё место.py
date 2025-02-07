def make_shades(alley: list[int], k: int) -> list[bool]:
    if k == 0:
        return [True if alley[i] else False for i in range(len(alley))]
    li = []
    i = 0
    temp = 0
    for i in range(len(alley)) if k > 0 else range(len(alley) - 1, -1, -1):
        if alley[i]:
            temp = max(temp, alley[i] * abs(k) + 1)
        if temp:
            li.append(True) if k > 0 else li.insert(0, True)
            temp -= 1
        else:
            li.append(False) if k > 0 else li.insert(0, False)
    return li


def calculate_sunny_length(shades: list[bool]) -> int:
    return shades.count(False)


def main():
    k = int(input())
    alley = list(map(int, input().split()))
    print('Обгорел' if calculate_sunny_length(make_shades(alley, k)) >= 10 else 'Тени достаточно')