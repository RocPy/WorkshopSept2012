'''
pngDisplay.py reads in a PNG image and displays it.
'''

import numpy
import pylab
import matplotlib.image

def readin(filename):
    im = matplotlib.image.imread(filename)
    return im

if __name__ == '__main__':
    filename = 'lena.png'
    im = readin(filename)
    pylab.figure(1)
    pylab.imshow(im)
    pylab.title('RGB')
    pylab.figure(2)
    pylab.gray()
    pylab.imshow(im[:,:,0]) # show red band
    pylab.title('Red')
    pylab.figure(3)
    pylab.imshow(im[:,:,1]) # show green band
    pylab.title('Green')
    pylab.figure(4)
    pylab.imshow(im[:,:,2]) # show blue band
    pylab.title('Blue')
    pylab.show()
