from django.utils.deprecation import MiddlewareMixin

class DefaultLanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            request.user.language_preference = "en"  # Set default language for anonymous users
