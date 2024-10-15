from django.utils.deprecation import MiddlewareMixin

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"Request Method: {request.method}, Path: {request.path}")
