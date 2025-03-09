def make_bingo():
    from random import shuffle
    nums = list(range(1, 76))
    shuffle(nums)

    def rand():
        return nums.pop()

    def row_gen():
        return tuple(rand() for _ in range(5))
    return row_gen(), row_gen(), (rand(), rand(), 0, rand(), rand()), row_gen(), row_gen()