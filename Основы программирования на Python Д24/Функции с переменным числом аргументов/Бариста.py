def choose_coffee(*preferences):
    coffee_recipes = {
        'Эспрессо': {0: 1},
        'Капучино': {0: 1, 1: 3},
        'Маккиато': {0: 2, 1: 1},
        'Кофе по-венски': {0: 1, 2: 2},
        'Латте Маккиато': {0: 1, 1: 2, 2: 1},
        'Кон Панна': {0: 1, 2: 1}
    }
    for coffee in preferences:
        save = ingredients[:] #  type: ignore
        for ingredient, quantity in coffee_recipes[coffee].items():
            ingredients[ingredient] -= quantity #  type: ignore
        if all([el > -1 for el in ingredients]): #  type: ignore
            return coffee
        ingredients[:] = save[:] #  type: ignore
    return 'К сожалению, не можем предложить Вам напиток'