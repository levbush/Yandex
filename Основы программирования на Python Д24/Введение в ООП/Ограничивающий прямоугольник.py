class BoundingRectangle:
    def __init__(self):
        self.points = []
        self.w = 0
        self.h = 0
        self.b_y = self.t_y = self.l_x = self.r_x = 0

    def add_point(self, x, y):
        w, h, b_y, t_y, l_x, r_x = self.w, self.h, self.b_y, self.t_y, self.l_x, self.r_x
        self.points.append((x, y))
        if len(self.points) == 1:
            self.l_x = self.r_x = x
            self.t_y = self.b_y = y
            return
        if x > r_x:
            self.r_x = x
            self.w += x - r_x
        elif x < l_x:
            self.l_x = x
            self.w += l_x - x
        if y > t_y:
            self.t_y = y
            self.h += y - t_y
        elif y < b_y:
            self.b_y = y
            self.h += b_y - y

    def width(self):
        return self.w

    def height(self):
        return self.h

    def bottom_y(self):
        return self.b_y

    def top_y(self):
        return self.t_y

    def left_x(self):
        return self.l_x

    def right_x(self):
        return self.r_x