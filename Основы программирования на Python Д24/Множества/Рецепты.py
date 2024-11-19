s = [input() for _ in range(int(input()))]
recipes = {input(): [input() for _ in range(int(input()))] for _ in range(int(input()))}
for recipe in recipes:
    if all(ingredient in s for ingredient in recipes[recipe]):
        print(recipe)