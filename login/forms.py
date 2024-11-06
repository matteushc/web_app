from django import forms


class NameForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60)
