import numpy, pylab, matplotlib
import sys
from scipy.optimize import curve_fit
from scipy.signal import argrelextrema

def polynomial(X, *coefficents):
	Y = numpy.zeros(numpy.shape(X))
	c = coefficents[0]
	print(c)
	for n in range(len(c)):
		k = c[n]
		Y += k*X**(len(c)-n-1)
	print(Y)
	return Y

def sinoidal(X, period, amplitude, offset, phase):
	return X * numpy.sin(X * period + phase) * amplitude + offset

guess_period = 2*numpy.pi
guess_amplitude = 1
guess_offset = 3
guess_phase = 0
p0 = [guess_period, guess_amplitude, guess_offset, guess_phase]


file_name = sys.argv[1]
DATA = numpy.loadtxt(file_name, delimiter=',')
DATA = DATA[numpy.logical_not(numpy.logical_or(DATA[:,13] > 0, DATA[:,26] > 0))]

stamps = DATA[:,0]/(60*1000000) # Convert to minutes
valid = DATA[:,13]

left_pupil = DATA[:,12]
right_pupil = DATA[:,25]
s = (left_pupil + right_pupil)/2

coef = numpy.polyfit(stamps, s, 20)
curve = polynomial(stamps, coef)#coef[0]*stamps**3 + coef[1]*stamps**2 + coef[2]*stamps + coef[3]
#sin_args = curve_fit(sinoidal, stamps, s, p0=p0)
#curve = sinoidal(stamps, *sin_args[0])



pylab.plot(stamps, s, 'c.', zorder=1)
pylab.plot(stamps, curve, 'g', zorder=2)

maxima = argrelextrema(curve, numpy.greater)
i = maxima[0]
print("Maxima found at: " + str(stamps[i]))
pylab.scatter(stamps[i], curve[i], color='red', s=15, zorder=3)

minima = argrelextrema(curve, numpy.less)
i = minima[0]
print("Minima found at: " + str(stamps[i]))
pylab.scatter(stamps[i], curve[i], color='blue', s=15, zorder=4)

pylab.xlim(0, 120)
pylab.ylim(-3, 7)
pylab.show()
