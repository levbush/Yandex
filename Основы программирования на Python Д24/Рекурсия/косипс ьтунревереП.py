def recursive_reverse(some_list):
    if some_list == []:
        return []
    if len(some_list) == 1:
        return some_list
    return recursive_reverse(some_list[1:]) + [some_list[0]]