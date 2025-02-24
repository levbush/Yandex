from sys import stdin
print(*sorted([line.rstrip() for line in stdin.readlines()], 
              key=lambda x: (sum([ord(i.upper()) for i in x]), x)), sep='\n')