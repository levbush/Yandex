from PIL import ImageDraw
from math import cos, sin, pi


class MyImageDraw(ImageDraw.ImageDraw):
    def regular_polygon(self, center_coords, sides, radius, rotation=0, fill=None, outline=None):
        self.polygon([(center_coords[0] + radius * cos(2 * pi * i / sides + rotation), 
                       center_coords[1] + radius * sin(2 * pi * i / sides + rotation)) for i in range(sides)],
                     fill=fill, outline=outline)