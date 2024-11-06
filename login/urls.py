from django.urls import path

from django.views.generic.base import TemplateView
from .views import loginView, send_login, logout_view


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("login/", loginView.as_view(), name="login"),
    path('send_login/', send_login, name='send_login'),
    path('logout/', logout_view, name='logout'),
]
