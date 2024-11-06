from django.urls import path

from django.views.generic.base import TemplateView
from .views import EstabelecimentoView, save


urlpatterns = [
    path("estabelecimento/", EstabelecimentoView.as_view(), name="estabelecimento"),
    path('save/', save, name='save'),
]
