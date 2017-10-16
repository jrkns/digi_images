import sys
from PIL import Image
import numpy as np

# P0 P1 P2
# P3 P4 P5
# P6 P7 P8

def med(array):
    length = len(array)
    if length%2 != 0:
        return array[(length//2)]
    return (array[(length//2)-1] + array[(length//2)]) // 2


def main(name):
    input_img = Image.open(name).convert('RGB')
    new_img = input_img.copy()
    w, h = input_img.size
    for x in range(w):
        for y in range(h):
            ignore = [False]*9
            P = [(0,0,0)]*9
            P[4] = input_img.getpixel((x,y))
            try:
                P[0] = input_img.getpixel((x-1,y-1))
            except:
                ignore[0] = True
            try:
                P[1] = input_img.getpixel((x,y-1))
            except:
                ignore[1] = True
            try:
                P[2] = input_img.getpixel((x+1,y-1))
            except:
                ignore[2] = True
            try:
                P[3] = input_img.getpixel((x-1,y))
            except:
                ignore[3] = True
            try:
                P[5] = input_img.getpixel((x+1,y))
            except:
                ignore[5] = True
            try:
                P[6] = input_img.getpixel((x-1,y+1))
            except:
                ignore[6] = True
            try:
                P[7] = input_img.getpixel((x,y+1))
            except:
                ignore[7] = True
            try:
                P[8] = input_img.getpixel((x+1,y+1))
            except:
                ignore[8] = True
            
            red = list()
            green = list()
            blue = list()
            for i in range (len(ignore)):
                if not ignore[i]:
                    red.append(P[i][0])
                    green.append(P[i][1])
                    blue.append(P[i][2])
            red = sorted(red)
            green = sorted(green)
            blue = sorted(blue)
            new_img.putpixel((x,y),(med(red),med(green),med(blue))) 
    # Save image
    new_img.save('out.png')
if __name__ == '__main__':
    try:
        main(sys.argv[-1])
    except:
        main('in.png')