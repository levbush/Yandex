stats = [int(input()) for _ in range(int(input()))]
trainings = [(int(input()), int(input()), int(input())) for _ in range(int(input()))]
brother1, brother2 = stats[:], stats[:]
for training in trainings:
    if training[0] == 1:
        brother1[training[1]] += training[2]
    else:
        brother2[training[1]] += training[2]
print(*brother1)
print(*brother2)
print(sum(1 for i in range(len(stats)) if brother1[i] == brother2[i]))