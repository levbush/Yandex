a = set()
b = set()
inp = input()
while inp:
    a.add(inp)
    inp = input()

inp = input()
while inp:
    b.add(inp)
    inp = input()
print(*(a & b) if (a & b) else ['EMPTY'], sep='\n')