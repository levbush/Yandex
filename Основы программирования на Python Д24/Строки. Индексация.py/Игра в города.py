word = input()
word2 = ''
while word[-1] == (word2 := input())[0]:
    word = word2
print(word2)
