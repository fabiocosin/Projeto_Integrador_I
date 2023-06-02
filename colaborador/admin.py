from django.contrib import admin
from .models import Colaborador

class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['nome_colaborador', 'cpf', 'rg', 'endereco', 'cep', 'municipio', 'data_nascimento', 'dependentes', 'cargo']

admin.site.register(Colaborador, ColaboradorAdmin)
