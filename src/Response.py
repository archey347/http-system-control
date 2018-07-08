import json

class Response:
	def __init__(self):
		self.headers = {
			"Content-type" : "text/json"
		}

		self.responseCode = 200
		self.body = ""

	def setHeader(self, name, value):
		for header in self.headers:
			if name == header:
				self.headers[name] = value

	def write(self, value):
		self.body = self.body + value

	def withJson(self, data):
		self.setHeader("Content-type", "application/json;charset=utf-8")

		self.body = json.dumps(data)
