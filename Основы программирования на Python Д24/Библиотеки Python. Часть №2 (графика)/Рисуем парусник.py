from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#87CEEB', ocean_color='#017B92', boat_color='#874535',
            sail_color='#FFFFFF', sun_color='#FFCF40'):
    img = Image.new('RGB', (width, height), sky_color)
    drawer = ImageDraw.Draw(img)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)), ocean_color)
    drawer.ellipse(((int(0.8 * width), -int(0.2 * height)), (int(1.2 * width), int(0.2 * height))), sun_color)
    drawer.polygon((int(width * 0.25), int(height * 0.65), (int(width * 0.3), int(height * 0.85)),
                    (int(width * 0.7), int(height * 0.85)), (int(width * 0.75), int(height * 0.65))), fill=boat_color)
    drawer.rectangle(((int(width * 0.49), int(height * 0.3)), (int(width * 0.51), int(height * 0.65))), boat_color)
    drawer.polygon(((int(width * 0.51), int(height * 0.3)), (int(width * 0.66), int(height * 0.45)),
                    (int(width * 0.51), int(height * 0.60))), fill=sail_color)
    img.save(file_name)