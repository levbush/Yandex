from collections import defaultdict


class SparseArray(defaultdict):
    def __init__(self):
        super().__init__(int)