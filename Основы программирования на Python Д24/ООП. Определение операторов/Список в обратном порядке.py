class ReversedList:
    def __init__(self, lst):
        self.contents = lst[::-1]

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, item):
        return self.contents[item]