from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
    email = models.CharField(max_length=100, verbose_name="Digite seu email")

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
   nome = models.CharField(max_length=50, verbose_name="Digite seu nome")
   cpf = models.CharField(max_length=11, verbose_name="Digite seu cpf")
   contato = models.CharField(max_length=50, verbose_name="Digite seu telefone")
   salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Digite seu salario")
   cargo = models.CharField(max_length=50, verbose_name="Digite seu cargo")
   horario = models.CharField(max_length=50, verbose_name="Digite o horario")
   cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Telefone(models.Model):
    numero = models.CharField(max_length=20, verbose_name="Digite seu telefone")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)

class Endereco(models.Model):
    logradouro = models.CharField(max_length=50, verbose_name="Digite seu logradouro")
    numero = models.CharField(max_length=4, verbose_name="Digite o numero de sua residencia")
    bairro = models.CharField(max_length=50, verbose_name="Digite seu bairro")
    cidade = models.CharField(max_length=50, verbose_name="Digite sua cidade")
    estado = models.CharField(max_length=50, verbose_name="Digite seu estado")
    pais = models.CharField(max_length=50, verbose_name="Digite seu país")
    cep = models.CharField(max_length=8, verbose_name="Digite o CEP")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)

class ContraCheque(models.Model):
    mes_de_referencia = models.IntegerField(verbose_name="Mês de referência")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

class Verbas(models.Model):
    proventos = models.IntegerField(verbose_name="Proventos do Mês de referência", default=0)
    descontos = models.IntegerField(verbose_name="Descontos do Mês de referência", default=0)
    demonstrativas = models.IntegerField(verbose_name="Demonstrativas do Mês de referência", default=0)

class PessoaFisica(models.Model):
    cpf = models.IntegerField(verbose_name="Digite o CPF")

class PessoaJuridica(models.Model):
    cnpj = models.IntegerField(verbose_name="Digite o CNPJ")
    razao_social = models.CharField(max_length=50, verbose_name="Digite a Razão Social")

class NotaFiscal(models.Model):
    numero = models.IntegerField(verbose_name="Numero da Nota Fiscal")
    data = models.DateField(verbose_name="Data da Nota Fiscal")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da Nota Fiscal")
    tipo = models.CharField(max_length=20, verbose_name="Tipo de Nota Fiscal")

class Proprietario(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do Proprietario")
    cpf = models.IntegerField(verbose_name="Digite o CPF")







