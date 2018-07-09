class Ping:
	def addRoutes(self, router):
		router.addRoute("GET", "/ping", self.ping)
		return router

	def ping(self, request, response):
		response.withJson({  
			"data": "pong"
		})
		return response
