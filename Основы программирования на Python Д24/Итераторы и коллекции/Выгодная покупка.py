from sys import stdin


headers = stdin.readline().strip('\n').strip('\n').split('\t')[1:]
text = stdin.readlines()
data = {line.strip('\n').split('\t')[0]: list(map(int, line.strip('\n').split('\t')[1:])) for line in text}
the_cheapest = min(data.items(), key=lambda x: sum(x[1]))[0]
print(the_cheapest)
print(*map(lambda x: f'{x[0]}\t{x[1]}', zip(headers, list(data[the_cheapest]))), sep='\n')