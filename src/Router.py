class Router:
	def __init__(self):
		self.routes = {}

	def addRoute(self, method, url, function):
		if not method in self.routes:
			self.routes[method] = {}
		self.routes[method][url] = function

	def executeRoute(self, request, response):
		return self.routes[request.method][request.path](request, response)
