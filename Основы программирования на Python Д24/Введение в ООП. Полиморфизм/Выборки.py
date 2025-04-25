class Selector:
    def __init__(self, nums):
        self.nums = nums[:]

    def get_odds(self):
        return list(filter(lambda x: x % 2, self.nums))

    def get_evens(self):
        return list(filter(lambda x: not x % 2, self.nums))