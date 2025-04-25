class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum([x ** i * self.coefficients[i] for i in range(len(self.coefficients))])

    def __add__(self, other):
        coefficients = [i + j for i, j in zip(self.coefficients, other.coefficients)] + (
            self.coefficients[len(other.coefficients):] if len(self.coefficients) >= len(
                other.coefficients) else other.coefficients[len(self.coefficients):])
        return Polynomial(coefficients)