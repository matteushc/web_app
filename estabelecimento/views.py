from django.shortcuts import render
from django.views import generic
from .forms import EstabForm
import requests


class EstabelecimentoView(generic.TemplateView):

    def get(self,request):
        return render(request,'estabelecimento.html')


def save(request):

    if request.method == 'POST':
        form = EstabForm(request.POST)
        if form.is_valid():
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"token {request.session["token"]}"
            }
            url = 'http://127.0.0.1:8000/estabelecimento/'
            myobj = {
                'nipcc': form.cleaned_data['nipcc'],
                'denominacao': form.cleaned_data['denominacao'],
                'sede_cep': form.cleaned_data['sede_cep'],
                'sede_endereco': form.cleaned_data['sede_endereco'],
                'cep_intervencao': form.cleaned_data['cep_intervencao'],
                'end_intervencao': form.cleaned_data['end_intervencao'],
                'email': form.cleaned_data['email'],
                'senha': form.cleaned_data['senha'],
                'confirmacao_senha': form.cleaned_data['confirmacao_senha'],
                'atv_id': form.cleaned_data['atv_id'],
                'obj_id': form.cleaned_data['obj_id'],
                'cid_id': form.cleaned_data['cid_id'],
                'dst_id': form.cleaned_data['dst_id'],
            }
            x = requests.post(url, json=myobj, headers=headers)

            return render(request, 'home.html')
