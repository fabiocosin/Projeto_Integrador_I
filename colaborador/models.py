from django.db import models

class Colaborador(models.Model):
    nome_colaborador = models.CharField(max_length=256)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    endereco = models.CharField(max_length=256)
    cep = models.CharField(max_length=9)
    municipio = models.CharField(max_length=256)
    data_nascimento = models.DateField()
    dependentes = models.IntegerField()
    cargo = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nome_colaborador
