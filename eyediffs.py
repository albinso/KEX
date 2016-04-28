import numpy, pylab, matplotlib
import sys

def calc_diffs(eye_pos):
	diffs = numpy.array([numpy.linalg.norm(eye_pos[i+1] - eye_pos[i]) for i in range(len(eye_pos)-1)])
	return diffs


file_name = sys.argv[1]
DATA = numpy.loadtxt(file_name, delimiter=',')
DATA = DATA[numpy.logical_not(numpy.logical_or(DATA[:,13] > 0, DATA[:,26] > 0))]

stamps = DATA[:,0]/(60*1000000)

l_raw = DATA[:,1:4]
r_raw = DATA[:,14:17]
left = calc_diffs(l_raw)
right = calc_diffs(r_raw)

pylab.subplot(2, 1, 1)
pylab.plot(stamps[:len(left)], left, 'g')
pylab.subplot(2, 1, 2)
pylab.plot(stamps[:len(right)], right, 'r')
pylab.xlim(2, 60)
pylab.ylim(2, 300)
pylab.show()

