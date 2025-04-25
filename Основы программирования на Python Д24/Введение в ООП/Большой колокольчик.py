class BigBell:
    is_ding = True

    def sound(self):
        print('ding') if self.is_ding else print('dong')
        self.is_ding = not self.is_ding