import numpy, pylab, matplotlib
import sys

file_name = sys.argv[1]
DATA = numpy.loadtxt(file_name, delimiter=',')
DATA = DATA[numpy.logical_not(numpy.logical_or(DATA[:,13] > 0, DATA[:,26] > 0))] # Remove invalid data

stamps = DATA[:,0]/(60*1000000) # Convert to minutes
valid = DATA[:,13]

left_pupil = DATA[:,12]
right_pupil = DATA[:,25]

pylab.plot(left_pupil, right_pupil, 'b.')
pylab.xlim(2, 7)
pylab.ylim(2, 7)
pylab.show()