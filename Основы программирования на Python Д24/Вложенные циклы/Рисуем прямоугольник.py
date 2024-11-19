h, w, border = int(input()), int(input()), input()
for i in range(h):
    if i == 0 or i == h - 1:
        row = border * w
    else:
        row = border + ' ' * (w - 2) + border
    print(row)