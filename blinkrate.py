from tobii.eye_tracking_io.browsing import EyetrackerBrowser
from tobii.eye_tracking_io.mainloop import MainloopThread, Mainloop
from tobii.eye_tracking_io.eyetracker import Eyetracker
from tobii.eye_tracking_io.types import GazeDataItem
from tobii.eye_tracking_io.types import Point2D
import tobii
import threading
import time
import sys


class BlinkRater:

	def __init__(self, length):
		self.length = length # time in seconds
		self.blink_counter = 0
		self.readings = 0
		self.isBlinking = False

	def StartTest(self):
		tobii.eye_tracking_io.init()
		ml = MainloopThread()
		et = EyetrackerBrowser(mainloop=ml, callback=self.OnBrowserEvent)

	def OnBrowserEvent(self, event_type, event_name, tracker_id):
		if event_type == tobii.eye_tracking_io.browsing.EyetrackerBrowser.FOUND:
			loop = MainloopThread()
			e = Eyetracker.create_async(loop, tracker_id, lambda error, eyetracker: self.OnNewTracker(error, eyetracker))

	def OnNewTracker(self, error, tracker):
		print("Found new tracker")
		self.tracker = tracker
		self.tracker.events.OnGazeDataReceived += self.OnGaze
		self.tracker.StartTracking(callback=self.OnGaze)

	def OnGaze(self, error, gaze):
		self.readings += 1
		if self.readings >= self.length*30:
			print("Blinks counted: " + str(self.blink_counter/2) + " in " + str(self.readings) + " readings.")
			sys.exit()
		if not self.isBlinking and gaze and self.CheckIfBlinking(gaze):
			self.isBlinking = True
			print("Blinked")
			self.blink_counter += 1
		elif gaze and not self.CheckIfBlinking(gaze):
			self.isBlinking = False

	def CheckIfBlinking(self, gaze):
		NO_DATA = Point2D(-1.0, -1.0)
		return compare(gaze.RightGazePoint2D, NO_DATA) and compare(gaze.LeftGazePoint2D, NO_DATA)


def compare(p1, p2):
	return p1.x == p2.x and p1.y == p2.y

br = BlinkRater(10)
br.StartTest()




