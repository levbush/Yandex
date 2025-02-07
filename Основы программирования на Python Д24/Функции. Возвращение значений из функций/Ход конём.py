def possible_turns(ceil: str) -> list:
    ceil = ord(list(ceil)[0]) - 64, int(list(ceil)[1])
    ans = []
    for dx in [-2, -1, 1, 2]:
        if dx % 2 == 0:
            for dy in [-1, 1]:
                if 0 < ceil[0] + dx < 9 and 0 < ceil[1] + dy < 9:
                    ans.append(chr(ceil[0] + dx + 64) + str(ceil[1] + dy))
        else:
            for dy in [-2, 2]:
                if 0 < ceil[0] + dx < 9 and 0 < ceil[1] + dy < 9:
                    ans.append(chr(ceil[0] + dx + 64) + str(ceil[1] + dy))
    return ans