import numpy, pylab, matplotlib
import sys

file_name = sys.argv[1]
DATA = numpy.loadtxt(file_name, delimiter=',')
DATA_VALID = DATA[numpy.logical_not(numpy.logical_or(DATA[:,13] > 0, DATA[:,26] > 0))]
DATA_INVALID = DATA[numpy.logical_not(numpy.logical_or(DATA[:,13] == 0, DATA[:,26] == 0))]


stamps = DATA[:,0]/(60*1000000) # Convert to minutes

pylab.plot(stamps)