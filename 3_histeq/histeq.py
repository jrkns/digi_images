from skimage import exposure
import sys
from PIL import Image
import numpy as np

def main(name):
    img = Image.open(name)
    img.load()
    data = np.asarray( img, dtype="int32" )
    img_eq_array = exposure.equalize_hist(data)
    img_eq = Image.fromarray(img_eq_array)
    img_eq.save('out.tiff')

if __name__ == '__main__':
    main('in.png')
