from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
    email = models.CharField(max_length=100, verbose_name="Digite seu email")
    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20, verbose_name="Digite seu telefone")

class Endereco(models.Model):
   logradouro = models.CharField(max_length=50, verbose_name="Digite seu logradouro")
   numero = models.CharField(max_length=4, verbose_name="Digite o numero de sua residencia")
   bairro = models.CharField(max_length=50, verbose_name="Digite seu bairro")
   cidade = models.CharField(max_length=50, verbose_name="Digite sua cidade")
   estado = models.CharField(max_length=50, verbose_name="Digite seu estado")
   pais = models.CharField(max_length=50, verbose_name="Digite seu país")
   cep = models.CharField(max_length=8, verbose_name="Digite o CEP")

