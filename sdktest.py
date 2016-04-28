from tobii.eye_tracking_io.browsing import EyetrackerBrowser
from tobii.eye_tracking_io.mainloop import MainloopThread, Mainloop
from tobii.eye_tracking_io.eyetracker import Eyetracker
from tobii.eye_tracking_io.types import GazeDataItem
from tobii.eye_tracking_io.types import Point2D
import tobii
import threading
import time


def loop_fun():
	while(True):
		a = threading.Event.wait()
		print("I got one!")
		print(a)

def print_dic(dic):
	for x in dic:
		print(x)
		for y in dic[x]:
			print (y,':',dic[x][y])


def new_tracker_callback(error, tracker, *args, **kwargs):
	print("Tracker: " + str(tracker))
	tracker.events.OnGazeDataReceived += track
	print("Bout to start tracking")
	print("Done calibrating")
	tracker.StartTracking(callback=track)
	print("Past tracking")

def track(error, gaze):
	#print("Tracking")
	if gaze and is_blinking(gaze):
		print("Blinked at " + str(gaze.Timestamp))

def is_blinking(gaze):
	NO_DATA = Point2D(-1.0, -1.0)
	return compare(gaze.RightGazePoint2D, NO_DATA) and compare(gaze.LeftGazePoint2D, NO_DATA)

def compare(p1, p2):
	return p1.x == p2.x and p1.y == p2.y



def backcall(event_type, event_name, tracker_id):
	if event_type == tobii.eye_tracking_io.browsing.EyetrackerBrowser.FOUND:
		print(event_type)
		print(event_name)
		loop = MainloopThread()
		e = Eyetracker.create_async(loop, tracker_id, lambda error, eyetracker: new_tracker_callback(error, eyetracker))
		print(e)

tobii.eye_tracking_io.init()
ml = MainloopThread()
print(type(ml))
et = EyetrackerBrowser(mainloop=ml, callback=backcall)



