last_row = [1]
row = [1]
for _ in range(int(input()) - 1):
    row = [1]
    for i in range(len(last_row) - 1):
        row.append(last_row[i] + last_row[i + 1])
    row.append(1)
    print(*last_row)
    last_row = row[:]
print(*row)