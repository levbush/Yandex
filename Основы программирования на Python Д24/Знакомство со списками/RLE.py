s = input()
last_i = s[0]
counter = 0
for i in s:
    if i == last_i:
        counter += 1
    else:
        print(counter, last_i)
        counter = 1
    last_i = i
print(counter, i)