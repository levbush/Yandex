class Balance:
    def __init__(self):
        self.left = self.right = 0

    def add_right(self, amount):
        self.right += amount

    def add_left(self, amount):
        self.left += amount

    def result(self):
        return 'L' if self.left > self.right else 'R' if self.right > self.left else '='