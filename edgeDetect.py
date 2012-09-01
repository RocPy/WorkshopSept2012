'''
edgeDetect.py reads in a PNG image and performs a Sobel edge detection
algorithm on it. It then displays the edge detected image.
'''

import numpy
import pylab
import matplotlib.image
import scipy.ndimage

def readin(filename):
    im = matplotlib.image.imread(filename)
    return im

def edgedet(array):
    edge = abs(scipy.ndimage.sobel(array))
    return edge

if __name__ == '__main__':
    filename = 'lena.png'
    im = readin(filename)
    pylab.figure(1)
    pylab.imshow(im)
    pylab.figure(2)
    pylab.gray()
    pylab.imshow(edgedet(im[:,:,0]))
    pylab.show()
