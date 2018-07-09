from http.server import BaseHTTPRequestHandler
from Request import Request
from Response import Response
from io import BytesIO

def makeRequestHandler(router):
	class requestHandler(BaseHTTPRequestHandler):
		def __init__(self, *args, **kwargs):
			super(requestHandler, self).__init__(*args, **kwargs)
			self.router = router		

		def handleRequest(self, method):
			request = Request(self, method)
			response = router.executeRoute(request, Response())
		
			self.send_response(response.responseCode)

			for header in response.headers:
				self.send_header(header, response.headers[header])

			self.end_headers()

			body = BytesIO()
			body.write(response.body.encode("utf8"))
			self.wfile.write(body.getvalue())
	
		def do_GET(self):
			self.handleRequest("GET")
	
	return requestHandler
