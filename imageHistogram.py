'''
imageHistogram.py reads in a PNG image and output a histogram of that image.
'''

import numpy
import pylab
import matplotlib.image

def readin(filename):
    im = matplotlib.image.imread(filename)
    return im

def hist(array, sym):
    #matplotlib.pyplot.hist(array.flatten(), 256, range=(0.0,1.0), fc='k', ec='k')
    (n, bins) = numpy.histogram(array.flatten(), bins=64)
    pylab.plot(.5*(bins[1:] + bins[:-1]), n, sym) 

if __name__ == '__main__':
    filename = 'lena.png'
    im = readin(filename)
    hist(im[:, :, 0], 'r-')
    hist(im[:, :, 1], 'g-')
    hist(im[:, :, 2], 'b-')
    pylab.title("Lena's Histogram")
    pylab.show()    

