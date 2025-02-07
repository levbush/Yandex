def diet(meals):
    meals = meals.split(', ')
    counter = sum([1 for meal in meals if meal not in food['диетическое']])  # type: ignore
    return 'Так держать, Воин Дракона!' if counter <= len(meals) // 2 else 'Не ешь столько, По!'