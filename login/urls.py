from django.urls import path

from django.views.generic.base import TemplateView
from .views import LoginView, send_login, logout_view


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path('send_login/', send_login, name='send_login'),
    path('logout/', logout_view, name='logout'),
]
