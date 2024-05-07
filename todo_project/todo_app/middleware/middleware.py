from django.contrib.auth.middleware import AuthenticationMiddleware

class CustomAuthenticationMiddleware(AuthenticationMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)

    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        )
        request.user = getattr(request, 'user', None)
        request.authenticated_microservice = False

        if request.user is None:
            request.user = self.authenticate(request)

    def authenticate(self, request):
        from django.contrib.auth import authenticate
        user = authenticate(request=request)
        if user:
            request.authenticated_microservice = True
        return user
