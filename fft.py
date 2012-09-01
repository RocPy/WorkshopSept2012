'''
fft.py calculates and plots the fast fourier transform of a function.
'''

import scipy
import numpy
import pylab

def step(transition, starts):
    x = numpy.arange(1000)
    y = numpy.zeros(1000)
    if starts == 0:
        y[transition:] = 1
    elif starts == 1:
        y[:transition] = 1
    X = numpy.arange(-500, 500, 1)
    Y = abs(numpy.fft.fft(y))
    _Y = numpy.zeros(1000)
    _Y[:500] = Y[500:]
    _Y[500:] = Y[:500]
    Y = _Y
    return x, y, X, Y

def squarewave(trans1, trans2, starts):
    x = numpy.arange(1000)
    if starts == 0:
        y = numpy.zeros(1000)
        y[trans1:trans2] = 1
    elif starts == 1:
        y = numpy.ones(1000)
        y[trans1:trans2] = 0
    X = numpy.arange(-500, 500, 1)
    Y = abs(numpy.fft.fft(y))
    _Y = numpy.zeros(1000)
    _Y[:500] = Y[500:]
    _Y[500:] = Y[:500]
    Y = _Y
    return x, y, X, Y

if __name__ == '__main__':
    pylab.suptitle('Functions and Their FFTs')
    pylab.subplot(221)
    Step = step(100, 0)
    pylab.title('Step Function')
    pylab.plot(Step[0], Step[1])
    pylab.subplot(222)
    Square = squarewave(450, 550, 0)
    pylab.title('Square Function')
    pylab.plot(Square[0], Square[1])
    pylab.subplot(223)
    pylab.title('FFT of Step Function')
    pylab.plot(Step[2], Step[3])
    pylab.subplot(224)
    pylab.title('FFT of Square Function')
    pylab.plot(Square[2], Square[3])
    pylab.show()
