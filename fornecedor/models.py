from django.db import models

class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=256)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=256)
    cep = models.CharField(max_length=9)
    municipio = models.CharField(max_length=256)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=256)
    nome_contato = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nome_fornecedor
