class Button:
    clicker = 0

    def click(self):
        self.clicker += 1

    def click_count(self):
        return self.clicker

    def reset(self):
        self.clicker = 0