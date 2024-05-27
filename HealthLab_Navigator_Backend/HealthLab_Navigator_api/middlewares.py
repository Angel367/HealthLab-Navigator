from django.utils.deprecation import MiddlewareMixin

class RemoveCOOPHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Cross-Origin-Opener-Policy'] = 'unsafe-none'
        return response