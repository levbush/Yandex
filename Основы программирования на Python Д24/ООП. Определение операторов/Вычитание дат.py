class Date:
    def __init__(self, month, day):
        self.month, self.day = month, day

    def __sub__(self, other):
        months_to_days_map = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self_days, others_days = sum(months_to_days_map[:self.month - 1]) + self.day, sum(
            months_to_days_map[:other.month - 1]) + other.day
        return self_days - others_days