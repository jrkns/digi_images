import sys
from PIL import Image

def main(name):
    input_img = Image.open(name).convert('RGB')
    w, h = input_img.size
    for x in range(w):
        for y in range(h):
            current = input_img.getpixel((x, y))
            grey = sum(current)//3 # Change formular here
            input_img.putpixel((x, y), (grey,grey,grey))
    # Save image
    input_img.save('out_hard.png')
if __name__ == '__main__':
    try:
        main(sys.argv[-1])
    except:
        main('in.png')