import numpy, pylab, matplotlib
import sys

file_name = sys.argv[1]
DATA = numpy.loadtxt(file_name, delimiter=',')
stamps = DATA[:,0]/(60*1000000)
#uniques = numpy.unique(stamps)
valid = DATA[:,13]

numpy.place(valid, valid != 4, [0])
numpy.place(valid, valid == 4, [1])
timeinterval = 30*60
count = 0
j = 0
a = numpy.empty((len(valid)/timeinterval))
for i in range(len(valid)):
	count += valid[i]
	if i >= timeinterval*(j+1):
		a[j] = count/30.0
		j += 1
		count = 0
print(a)
pylab.plot(range(len(a)), a)
pylab.show()