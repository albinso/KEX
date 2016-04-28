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




#plot_time(stamps[:len(left_pupil)], left_pupil.T, 'r')
#plot_time(stamps[:len(right_pupil)], right_pupil.T, 'g')
plot_time(stamps, valid, 'b.')
pylab.xlim(0, 60)
pylab.ylim(-1, 2)
pylab.show()