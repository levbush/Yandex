from PIL import Image, ImageDraw
from random import choice


img = Image.new('RGB', (500, 200), color='green')
draw = ImageDraw.Draw(img)
draw.line(((90, 0), (10, 200)), fill='#0bc693', width=5)
draw.line(((90, 0), (170, 200)), fill='#0bc693', width=5)
colours = [(200, 50, 50), (50, 50, 200), (200, 200, 50), (200, 50, 200), (50, 200, 200), 
           (150, 100, 50), (100, 150, 50), (50, 150, 100), (150, 50, 100), (100, 50, 150), (255, 165, 0),
           (128, 0, 128), (0, 128, 128), (255, 192, 203), (255, 215, 0)]
for i in range(5):
    if i % 2 == 0:
        for j in range(3):
            draw.ellipse((200 + 40 * j, 5 + 40 * i, 240 + 40 * j, 40 + 40 * i), fill=choice(colours))
    else:
        draw.ellipse((200, 5 + 40 * i, 240, 40 + 40 * i), fill=choice(colours))

draw.rectangle((375, 0, 400, 200), fill='#0bc693')
draw.arc((300, 0, 500, 100), 270, 90, fill=choice(colours), width=20)
draw.arc((300, 100, 500, 200), 270, 90, fill=choice(colours), width=20)
img.save('name.png')