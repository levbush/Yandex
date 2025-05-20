from itertools import groupby
from sys import stdin


data = list(zip(*[el.split() for el in stdin.readlines()]))
capitals, citizens = data[0], {data[0][i]: int(data[2][i]) for i in range(len(data[2]))}

print(
    *list(
        map(
            lambda x: f'{x[0]}: {', '.join(sorted(x[1]))}',
            groupby(
                sorted(capitals, key=lambda x: citizens[x]),
                lambda x: f'{citizens[x] // 100000 * 100} - {citizens[x] // 100000 * 100 + 100}'
            )
        )
    ),
    sep='\n'
)