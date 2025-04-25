class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{str(self.month).rjust(2, "0")}.{str(self.day).rjust(2, "0")}.{self.year}'

    def set_year(self, n):
        self.year = n

    def set_month(self, n):
        self.month = n

    def set_day(self, n):
        self.day = n

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day


class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{str(self.day).rjust(2, "0")}.{str(self.month).rjust(2, "0")}.{self.year}'

    def set_year(self, n):
        self.year = n

    def set_month(self, n):
        self.month = n

    def set_day(self, n):
        self.day = n

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day