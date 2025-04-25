class MinStat:
    def __init__(self):
        self.seq = []

    def add_number(self, number):
        self.seq.append(number)

    def result(self):
        return min(self.seq) if self.seq else None


class MaxStat:
    def __init__(self):
        self.seq = []

    def add_number(self, number):
        self.seq.append(number)

    def result(self):
        return max(self.seq) if self.seq else None


class AverageStat:
    def __init__(self):
        self.seq = []

    def add_number(self, number):
        self.seq.append(number)

    def result(self):
        return sum(self.seq) / len(self.seq) if self.seq else None