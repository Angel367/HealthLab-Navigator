from django.utils.deprecation import MiddlewareMixin

class RemoveCOOPHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if 'Cross-Origin-Opener-Policy' in response:
            del response['Cross-Origin-Opener-Policy']
        return response