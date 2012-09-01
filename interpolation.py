'''
interpolation.py demonstrates how numpy can be used to interpolate points
by solving a system of equations describing a polynomial.
Introduces the Vandermonde matrix.
'''

import numpy
import pylab

pts = [(1, 2), (2, 3), (3, 6)]
# Vandermonde Matrix
a = numpy.array([[1, pts[0][0], pts[0][0]**2],
                 [1, pts[1][0], pts[1][0]**2],
                 [1, pts[2][0], pts[2][0]**2]])
b = numpy.array([pts[0][1], pts[1][1], pts[2][1]])
x = numpy.linalg.solve(a, b)
print x
print (numpy.dot(a, x) == b).all()
for i in range(len(pts)):
    pylab.plot(pts[i][0], pts[i][1], 'ro')
X = numpy.arange(0, 4, .01)
pylab.plot(X, x[0] + x[1]*X + x[2]*X**2, 'b-')
pylab.show()

