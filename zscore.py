'''
zscore.py calculates and plots the probability given the zscore on a standard
normal probability density function.
'''

import numpy
from scipy.integrate import quad, inf
import pylab

delta_x = .00001
range_x = 10.0
zscore = 1.5

x = numpy.arange(-range_x,range_x, delta_x)
norm = lambda a: 1/numpy.sqrt(2*numpy.pi)*numpy.exp(-(a)**2/2)
prob = quad(norm,zscore,inf)[0]
upto = numpy.piecewise(x,[x<zscore,x>=zscore],[0, norm])
pylab.fill(x, upto, 'r', alpha = 0.3)
pylab.plot(x,norm(x))
pylab.title('Z-Score Plot')
pylab.xlabel('Z-Score')
pylab.ylabel('Probability Density')
pylab.text(1.0, 0.35, 'For a Z-Score of ' + '%1.4f' %zscore + '\nthe probability is ' + '%1.4f' %prob, fontsize=12)
pylab.xlim(-5,5)
pylab.show()
