def recursive_len(some_list):
    if some_list == []:
        return 0
    return recursive_len(some_list[1:]) + 1