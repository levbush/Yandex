from itertools import permutations


dictionary = input().lower().split()
letter = input().lower().split()
for i in range(len(letter)):
    word = letter[i]
    for perm in permutations(word):
        if ''.join(perm) in dictionary and ''.join(perm) != word:
            letter[i] = '#' * len(word)
print(*letter)