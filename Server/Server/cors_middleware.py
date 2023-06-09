class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response["Access-Control-Allow-Origin"] = request.headers.get("Origin")
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response[
            "Access-Control-Allow-Headers"
        ] = "Origin, X-Requested-With, Content-Type, Accept, Authorization, X-CSRFToken"
        response["Access-Control-Allow-Credentials"] = "true"

        return response
