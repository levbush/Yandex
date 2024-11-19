n, s = int(input()), input()
ords = [ord(i) for i in s]
for i in range(len(ords)):
    if 1039 < ords[i] < 1072:
        ords[i] += n
        if ords[i] > 1071:
            ords[i] -= 32
    elif 1071 < ords[i] < 1104:
        ords[i] += n
        if ords[i] > 1103:
            ords[i] -= 32
print(''.join([chr(i) for i in ords]))
