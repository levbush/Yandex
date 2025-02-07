def count_food(days):
    return sum(daily_food[i - 1] for i in days)  # type: ignore