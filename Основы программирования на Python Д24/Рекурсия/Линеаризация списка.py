def linear(some_list):
    if some_list == []:
        return []
    if isinstance(some_list[0], list):
        if len(some_list) == 1:
            return linear(some_list[0])
        return linear(some_list[0]) + linear(some_list[1:])
    if len(some_list) > 1:
        return [some_list[0]] + linear(some_list[1:])
    return [some_list[0]]