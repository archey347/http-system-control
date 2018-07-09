from daemon import Daemon
from Router import Router
import requestHandler
import time
from http.server import HTTPServer

from Ping import Ping


class Service(Daemon):
	def run(self):
		router = Router()


		ping = Ping()

		router = ping.addRoutes(router)

		handler = requestHandler.makeRequestHandler(router)
		httpd = HTTPServer(('192.168.0.82', 8000), handler)
		httpd.serve_forever()

