class Request:
	def __init__(self, request, method):
		self.path = request.path
		self.headers = request.headers
		self.method = method
		self.client_address = request.client_address
		
