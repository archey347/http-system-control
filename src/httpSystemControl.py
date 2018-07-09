from daemon import Daemon
from Router import Router
import requestHandler
import time
from http.server import HTTPServer

def hello_world(request, response):
	response.write("Hello World :)")
	return response


class Service(Daemon):
	def run(self):
		router = Router()
		router.addRoute("GET", "/", hello_world)


		handler = requestHandler.makeRequestHandler(router)
		httpd = HTTPServer(('192.168.0.82', 8000), handler)
		httpd.serve_forever()

