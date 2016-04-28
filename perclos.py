import numpy, pylab, matplotlib
import sys

file_name = sys.argv[1]
DATA = numpy.loadtxt(file_name, delimiter=',')
stamps = DATA[:,0]/(60*1000000)
#uniques = numpy.unique(stamps)
valid = DATA[:,13]


numpy.place(valid, valid != 4, [0])
numpy.place(valid, valid == 4, [1])

#pair = numpy.array([(stamps[i], valid[i]) for i in range(len(stamps))], dtype=[('time', numpy.uint32), ('valid', numpy.uint8)])


#res = matplotlib.mlab.rec_groupby(pair, ('time',), (('valid', count_spec, 'val_count'),))
#print(res[:][0])

def plot_time(time, vals, c):
	pylab.plot(time, vals, c)
	#pylab.plot([-10, stamps[-1]+10], [-1, 5])

closed = 0.0
for i in valid:
	if i != 0:
		closed += 1.0

print closed/len(valid)
