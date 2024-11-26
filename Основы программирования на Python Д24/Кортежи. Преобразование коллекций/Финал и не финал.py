teams = sorted((input(), int(input())) for _ in range(int(input())))
teams_answer = teams[:]
mean = sum([i[1] for i in teams]) / len(teams)
for team in teams:
    if mean <= team[1]:
        print(team[0])
        teams_answer.remove(team)
print(*sorted([i[0] for i in teams_answer]), sep='\n')
