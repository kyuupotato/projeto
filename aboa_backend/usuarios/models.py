from django.db import models
from django.contrib.auth.models import User

class Estabelecimento(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    razao_social = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
    inscricao_estadual = models.CharField(max_length=50, blank=True)
    isento_ie = models.BooleanField(default=False)
    ramo_atividade = models.CharField(max_length=100)

    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_fantasia
