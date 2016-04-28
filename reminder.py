import time
import os

path = '~/Downloads/beep-01a.wav'
os.system('play %s' % path)
interval = 900
mom = 1
os.system("beep -f 555 -l 460")
print(str(mom)*10)
while True:
	time.sleep(interval)
	#for i in range(0, 100):
		#print(str(mom)*10)
	os.system('play %s' % path)

	mom = mom+1