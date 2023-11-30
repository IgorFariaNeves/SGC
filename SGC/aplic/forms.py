# forms.py
from django import forms

class FuncionarioSearchForm(forms.Form):
    nome = forms.CharField(label='Nome do Funcionário', required=False)
