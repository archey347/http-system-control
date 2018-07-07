from daemon import Daemon
import time

class Service(Daemon):
	def run(self):
		while True:
			time.sleep(10) 

