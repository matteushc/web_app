from django import forms


class EstabForm(forms.Form):
    nipcc = forms.CharField(max_length=60)
    denominacao = forms.CharField(max_length=60)
    sede_cep = forms.CharField(max_length=60)
    sede_endereco = forms.CharField(max_length=60)
    cep_intervencao = forms.CharField(max_length=60)
    end_intervencao = forms.CharField(max_length=60)
    email = forms.CharField(max_length=60)
    senha = forms.CharField(max_length=60)
    confirmacao_senha = forms.CharField(max_length=60)
    atv_id = forms.IntegerField()
    obj_id = forms.IntegerField()
    cid_id = forms.IntegerField()
    dst_id = forms.IntegerField()
