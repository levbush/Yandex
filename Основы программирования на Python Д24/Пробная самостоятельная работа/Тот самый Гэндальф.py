counter = 0
while 'Гэндальф' not in (inp := input()):
    if 'волшебн' in inp:
        counter += len(inp)
print(counter)