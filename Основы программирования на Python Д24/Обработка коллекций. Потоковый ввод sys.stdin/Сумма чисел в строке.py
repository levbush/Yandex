from sys import stdin


nums = []
for line in stdin.readlines():
    line_sum = 0
    counter = 0
    for el in line.split():
        if el.isdigit():
            line_sum += int(el)
            counter += 1
    nums.append((-counter, line_sum))
print(min(nums or [0])[-1] or -1)