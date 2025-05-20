from itertools import product, combinations


suits = ['бубен', 'пик', 'треф', 'червей']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
elders = ['валет', 'дама', 'король', 'туз']
cards = set()
for perm in combinations(product(ranks, suits), 3):
    if not any(card[0] in elders for card in perm) or not any(card[1] == 'червей' for card in perm):
        continue
    cards.add(', '.join(f"{rank} {suit}" for rank, suit in sorted(perm)))

print(*sorted(cards), sep='\n')