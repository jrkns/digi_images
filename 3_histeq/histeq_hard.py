from PIL import Image
import numpy as np
import math

# Algorithm
def equalize_hist(img):
    data = img.copy().flatten()
    histogram = [0]*256
    for pixel in data:
        histogram[pixel] += 1
    cdf = [0]*256
    for i in range (len(histogram)):
        cdf[i] = sum(histogram[0:i+1])
    
    prob_of_cdf = [0]*256
    for i in range (len(cdf)):
        prob_of_cdf[i] = cdf[i]/cdf[-1]
    
    new_map = [0]*256
    for i in range (len(new_map)):
        new_map[i] = math.floor(prob_of_cdf[i]*255)

    new_img = np.array([[0]*len(img[0])]*len(img), dtype=np.uint8)
    for x in range (len(img)):
        for y in range (len(img[0])):
            new_img[x][y] = new_map[img[x][y]]
    return new_img

if __name__ == '__main__':
    img = Image.open('in.png')
    img.load()
    data = np.asarray( img, dtype=np.uint8 )
    img_eq = Image.fromarray(equalize_hist(data), mode='L')
    img_eq.save('out_hard.png')
    