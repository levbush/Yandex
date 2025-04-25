from PIL import Image, ImageDraw


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.colors = {el: 'black' for el in sum(self.draw_map, [])}

    def numbers(self):
        return list(self.colors.values())
    
    def set_color(self, number, color):
        self.colors[number] = color
    
    def set_cell_size(self, cell_size):
        self.cell_size = cell_size
    
    def size(self):
        return self.cell_size * len(self.draw_map[0]), self.cell_size * len(self.draw_map)
    
    def draw(self):
        img = Image.new('RGB', self.size(), 'black')
        draw = ImageDraw.Draw(img)
        for row in range(len(self.draw_map)):
            for color in range(len(self.draw_map[row])):
                draw.rectangle(((self.cell_size * color, self.cell_size * row), 
                                (self.cell_size * (color + 1), self.cell_size * (row + 1))),
                               self.colors[self.draw_map[row][color]])
        return img