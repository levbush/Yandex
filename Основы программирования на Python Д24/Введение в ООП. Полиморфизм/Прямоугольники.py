class Rectangle:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def intersection(self, rect):
        new_x = max(self.x, rect.x)
        new_xw = min(self.x + self.w, rect.x + rect.w)
        new_y = max(self.y, rect.y)
        new_yh = min(self.y + self.h, rect.y + rect.h)
        if new_xw > new_x and new_yh > new_y:
            return Rectangle(new_x, new_y, new_xw - new_x, new_yh - new_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_h(self):
        return self.h

    def get_w(self):
        return self.w