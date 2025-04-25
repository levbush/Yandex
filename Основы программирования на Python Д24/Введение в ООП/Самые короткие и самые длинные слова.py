class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence: str):
        self.words += sentence.split()

    def shortest_words(self):
        return sorted(list(filter(lambda x: len(x) == len(min(self.words, key=len)), self.words)))

    def longest_words(self):
        return sorted(set(list(filter(lambda x: len(x) == len(max(self.words, key=len)), self.words))))