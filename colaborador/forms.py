from django import forms
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome_colaborador', 'cpf', 'rg', 'endereco', 'cep', 'municipio', 'data_nascimento', 'dependentes', 'cargo']
