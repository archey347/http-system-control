class Router:
	def __init__(self):
		self.router = {}

	def addRoute(self, method, url, function):
		self.router[method][url] = function

	def exexuteRoute(self, method, url):
		return self.router[method][url]()
