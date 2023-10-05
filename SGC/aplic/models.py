from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
    email = models.CharField(max_length=100, verbose_name="Digite seu email")
    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20, verbose_name="Digite seu telefone")

#class Endereco(models.Model):
#   logradouro = models.CharField(max_length=50, verbose_name=)