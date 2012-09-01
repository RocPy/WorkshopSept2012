'''
polyfit.py demonstrates the use of Numpy's polyfit least squares curve fitting.
'''

import numpy
import pylab

order = 4
x = numpy.linspace(0, 2*numpy.pi, 10)
y = 0.01 * numpy.random.random(10) + numpy.sin(x)
fit = numpy.polyfit(x, y, order)
print fit
X = numpy.linspace(0, 2*numpy.pi, 100)
polys = []
FIT = numpy.ones((order + 1) *  100).reshape(order + 1, 100)
for i in range(order + 1):
    polys.append(X**(order-i))
    FIT[i][:] = fit[i]
Y = polys*FIT
_Y = numpy.zeros(100)
for i in range(order + 1):
    _Y = _Y + Y[i]
# Y = fit[0]*X**3 + fit[1]*X**2 + fit[2]*X + fit[3]
pylab.plot(x, y, 'ro')
pylab.plot(X, _Y, 'b-')
pylab.show()
