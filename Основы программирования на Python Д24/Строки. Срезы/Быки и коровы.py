s1, s2 = list(input()), list(input())
oxe = cow = 0
for i in range(len(s1)):
    if s1[i] == s2[i]:
        oxe += 1
    elif s1.count(s1[i]) == s2.count(s1[i]):
        cow += 1
print(oxe, cow)