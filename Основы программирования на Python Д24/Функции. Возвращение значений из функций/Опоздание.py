def find_closest_smaller(value: int, array: list[int]) -> int:
    diff = float('inf')
    array.sort()
    closest = None
    for el in array:
        if value - el < diff:
            if value >= el >= 5:
                diff = value - el
                closest = el
        else:
            return el
    return closest


def late(now: str, classes: str, bus: list[int]) -> str:
    from datetime import timedelta
    now: timedelta = timedelta(hours=int(now.split(':')[0]), minutes=int(now.split(':')[1]))
    classes: timedelta = timedelta(hours=int(classes.split(':')[0]), minutes=int(classes.split(':')[1]))
    if classes - now < timedelta(minutes=20):
        return 'Опоздание'
    min_to_bus = (classes - now - timedelta(minutes=15)).seconds // 60
    ans = find_closest_smaller(min_to_bus, bus)
    return f'Выйти через {ans - 5} минут' if ans else 'Опоздание'