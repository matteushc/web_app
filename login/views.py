from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .forms import NameForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import requests

# Create your views here.


class loginView(generic.TemplateView):

    def get(self,request):
        return render(request,'login.html')


def logout_view(request):
    logout(request)
    return render(request,'login.html')


def send_login(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            url = 'http://127.0.0.1:8000/api-token-auth/'
            myobj = {
                'username': form.cleaned_data['username'],
                'password': form.cleaned_data['password']
            }
            x = requests.post(url, json=myobj)
            authentication_json = x.json()
            if authentication_json.get('token'):
                try:
                    user = User.objects.get(username=form.cleaned_data['username'])
                except ObjectDoesNotExist:
                    user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['username'], form.cleaned_data['password'])
                login(request, user)
                return render(request,'home.html')
            else:
                return render(request,'login.html')

