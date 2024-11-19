def rec_linear_sum(some_list):
    if some_list == []:
        return 0
    return rec_linear_sum(some_list[1:]) + some_list[0]