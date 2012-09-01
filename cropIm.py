'''
cropIm.py reads in a png image and crops it to specific corner points. It
then displays the cropped image.
'''

import numpy
import pylab
import matplotlib.image

def readin(filename):
    im = matplotlib.image.imread(filename)
    return im

def crop(array, UL, LR):
    croparr = array[UL[0]:LR[0]+1, UL[1]:LR[1]+1, :]
    return croparr

if __name__ == '__main__':
    filename = 'lena.png'
    im = readin(filename)
    pylab.subplot(121)
    pylab.imshow(im)
    UL = (200, 175)
    LR = (400, 400)
    pylab.subplot(122)
    pylab.imshow(crop(im, UL, LR))
    pylab.show()
