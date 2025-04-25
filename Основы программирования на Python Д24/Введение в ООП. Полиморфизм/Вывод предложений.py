class LeftParagraph:
    def __init__(self, line_len):
        self.cursor = [0, 0]
        self.max_length = line_len
        self.container = ['']

    def add_word(self, word):
        if self.cursor[1] + (1 if self.cursor[1] else 0) + len(word) > self.max_length:
            self.cursor = [self.cursor[0] + 1, 0]
            self.container.append('')
        self.container[self.cursor[0]] += (' ' if self.cursor[1] else '') + word
        self.cursor[1] += len(word) + (1 if self.cursor[1] else 0)

    def end(self):
        print(*self.container, sep='\n')
        self.__init__(self.max_length)


class RightParagraph:
    def __init__(self, line_len):
        self.cursor = [0, 0]
        self.max_length = line_len
        self.container = ['']

    def add_word(self, word):
        if self.cursor[1] + (1 if self.cursor[1] else 0) + len(word) > self.max_length:
            self.cursor = [self.cursor[0] + 1, 0]
            self.container.append('')
        self.container[self.cursor[0]] += (' ' if self.cursor[1] else '') + word
        self.cursor[1] += len(word) + (1 if self.cursor[1] else 0)

    def end(self):
        [print(line.rjust(self.max_length)) for line in self.container]
        self.__init__(self.max_length)
