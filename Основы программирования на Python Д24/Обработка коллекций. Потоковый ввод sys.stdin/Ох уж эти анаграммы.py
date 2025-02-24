from sys import stdin
from collections import defaultdict


length = int(input())
data = sorted([line.strip().lower() for line in stdin.readlines()])
anagrams = defaultdict(set)
for word in data:
    sorted_word = ''.join(sorted(word))
    anagrams[sorted_word].add(word)
for group in anagrams.values():
    if len(group) > 1:
        print(*sorted(group))