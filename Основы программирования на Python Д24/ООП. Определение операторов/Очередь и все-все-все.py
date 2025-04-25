class Queue:
    def __init__(self, *seq):
        self.elements = list(seq).copy()

    def append(self, *els):
        self.elements += list(els)

    def copy(self):
        return Queue(*self.elements[:])

    def pop(self):
        if self.elements:
            return self.elements.pop(0)

    def extend(self, queue: 'Queue'):
        self.append(*queue.elements)

    def next(self):
        return Queue(*self.elements[1:])

    def __add__(self, other):
        return Queue(*(self.elements + other.elements))

    def __iadd__(self, other):
        self.elements += other.elements
        return self

    def __eq__(self, other):
        return self.elements == other.elements

    def __rshift__(self, n):
        return Queue(*self.elements[n:])

    def __str__(self):
        result = '['
        for el in self.elements:
            result += f' -> {el}' if result != '[' else str(el)
        return result + ']'

    def __next__(self):
        return Queue(*self.elements[1:])