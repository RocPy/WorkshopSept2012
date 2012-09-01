import numpy
import pylab

a = numpy.arange(0,100*100, 1).reshape(100, 100)
pylab.imshow(a)
pylab.show()

