from PIL import Image
import random as rd
from collections import deque
import sys

WHITE = 255, 255, 255
BLACK = 0, 0, 0

def gen_colors(n):
    colors = []
    i = 0
    while i < n:
        color = (rd.randrange(255),rd.randrange(255),rd.randrange(255))
        if color != BLACK and color != WHITE:
            colors.append(color)
            i += 1
    return colors

def main(name):
    input_img = Image.open(name).convert('RGB')
    w, h = input_img.size
    colors = gen_colors(100)
    i = 0
    for x in range(w):
        for y in range(h):
            current = input_img.getpixel((x, y))
            if current not in colors:
                flood_fill(x, y, colors[i], input_img, w, h)
                if i + 1 >= len(colors):
                    break
                i += 1
    # Save image
    input_img.save('out.png')

def flood_fill(x, y, color, image, w, h):
    source = image.getpixel((x, y))
    if source != color:
        pixels = deque([(x, y)])
        while pixels:
            x, y = place = pixels.popleft()
            image.putpixel(place, color)
            for x_offset in -1,0,1:
                x_offset += x
                for y_offset in -1,0,1:
                    y_offset += y
                    new_place = x_offset, y_offset
                    if x_offset < 0 or x_offset >= w or y_offset < 0 or y_offset >= h:
                        continue
                    if image.getpixel(new_place) == source and new_place not in pixels:
                        pixels.append(new_place)

if __name__ == '__main__':
    try:
        main(sys.argv[-1])
    except:
        main('in.png')