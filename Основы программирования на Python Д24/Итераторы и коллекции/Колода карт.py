from itertools import product


suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(input())
denominations = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

print(*map(lambda x: f'{x[0]} {x[1]}', sorted(product(denominations, suits), 
                                              key=lambda x: (denominations.index(x[0]), suits.index(x[1])))), sep='\n')