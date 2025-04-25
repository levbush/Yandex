class OddEvenSeparator:
    def __init__(self):
        self.even_nums, self.odd_nums = [], []

    def add_number(self, number):
        if number % 2 == 0:
            self.even_nums.append(number)
        else:
            self.odd_nums.append(number)
    
    def even(self):
        return self.even_nums
    
    def odd(self):
        return self.odd_nums