import sys
from PIL import Image

def main(name):
    img = Image.open(name).convert('LA')
    img.save('out.png')

if __name__ == '__main__':
    try:
        main(sys.argv[-1])
    except:
        main('in.png')