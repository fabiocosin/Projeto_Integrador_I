from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_fornecedor', 'cnpj', 'endereco', 'cep', 'municipio', 'telefone', 'celular', 'email', 'nome_contato']
