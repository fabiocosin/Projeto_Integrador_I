from django.contrib import admin
from .models import Fornecedor

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome_fornecedor', 'cnpj', 'endereco', 'cep', 'municipio', 'telefone', 'celular', 'email', 'nome_contato']

admin.site.register(Fornecedor, FornecedorAdmin)
