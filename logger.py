from tobii.eye_tracking_io.browsing import EyetrackerBrowser
from tobii.eye_tracking_io.mainloop import MainloopThread, Mainloop
from tobii.eye_tracking_io.eyetracker import Eyetracker
from tobii.eye_tracking_io.types import GazeDataItem
from tobii.eye_tracking_io.types import Point2D
import tobii
import threading
import thread
import time
import sys
from Queue import Queue, Empty
from cam import cammy


class Logger:

	def __init__(self):
		self.gazeData = Queue()
		self.running = True
		self.mode = 'w'
		self.origin_time = 0

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
		print("About to start logging")
		thread.start_new_thread(self.StartLogging, ())
		print("Started logging")
		self.tracker.StartTracking(callback=self.OnGaze)
		print("Done with new tracker")

	def OnGaze(self, error, gaze):

		if(gaze != None):
			if self.origin_time == 0:
				self.origin_time = gaze.Timestamp
			gaze.Timestamp = gaze.Timestamp - self.origin_time
			self.gazeData.put(gaze)


	def StartLogging(self):
		
		while self.running:
			with open('gaze.log', self.mode) as f:
				self.mode = 'a'
				try:
					f.write(self.toText(self.gazeData.get(block=True, timeout=15)))
				except Empty:
					print("Stopping")
					self.running = False

	def toText(self, gaze):
		return str(gaze) + '\n'

br = Logger()
br.StartTest()
cammy()




