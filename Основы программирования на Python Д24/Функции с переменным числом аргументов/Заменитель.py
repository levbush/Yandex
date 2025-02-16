def placeholder(*lines, **holders):
    from collections import defaultdict
    ans = defaultdict(list)
    lines: tuple[str]
    holders: dict[str, str]
    for holder in holders.values():
        holder = holder.split()
        for line in lines:
            line = line.split()
            if len(line) != len(holder):
                continue
            for i in range(len(line)):
                if holder[i] == '|_':
                    if line[i] != line[i].capitalize() or not line[i].isalpha():
                        break
                elif holder[i] == '_':
                    if not line[i].isalpha() or not line[i].islower():
                        break
                elif line[i][-1] != holder[i][-1]:
                    break
            else:    
                ans[' '.join(holder)].append(' '.join(line))
                ans[' '.join(holder)].sort()
    return ans