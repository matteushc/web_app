import re

from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout


EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/')), re.compile(settings.CHECK_LOGIN_URL.lstrip('/'))]


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if not request.user.is_authenticated and not url_is_exempt:
            return redirect("login")