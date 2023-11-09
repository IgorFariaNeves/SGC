from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    email = models.CharField(max_length=100, verbose_name="Email")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class PessoaFisica(Cliente):
    cpf = models.CharField(max_length=11, verbose_name="CPF")

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Pessoa Física"
        verbose_name_plural = "Pessoas Físicas"
        default_related_name = "pessoafisica"

class Proprietario(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do Proprietário")
    cpf = models.CharField(max_length=11, verbose_name="CPF")

    class Meta:
        verbose_name = "Proprietário"
        verbose_name_plural = "Proprietários"

class PessoaJuridica(Cliente):
    cnpj = models.CharField(max_length=14, verbose_name="CNPJ")
    razao_social = models.CharField(max_length=50, verbose_name="Razão Social")
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa Jurídica"
        verbose_name_plural = "Pessoas Jurídicas"
        default_related_name = "pessoajuridica"

class NotaFiscal(models.Model):
    TIPO_CHOICES = (
        ('entrada', 'Entrada'),
        ('saída', 'Saída'),
    )

    numero = models.IntegerField(verbose_name="Número da Nota Fiscal")
    data = models.DateField(verbose_name="Data da Nota Fiscal")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da Nota Fiscal")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo de Nota Fiscal")
    pessoajuridica = models.ForeignKey(PessoaJuridica, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"Nota Fiscal - {self.numero}"

    class Meta:
        verbose_name = "Nota Fiscal"
        verbose_name_plural = "Notas Fiscais"

class Funcionario(models.Model):
   nome = models.CharField(max_length=50, verbose_name="Nome")
   cpf = models.CharField(max_length=11, verbose_name="CPF")
   data_nascimento = models.DateField(verbose_name="Data de Nascimento", null=True)
   salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salário")
   cargo = models.CharField(max_length=50, verbose_name="Cargo")
   horario_entrada = models.TimeField(verbose_name="Horário de Entrada", help_text='HH:MM', null=True)
   horario_saida = models.TimeField(verbose_name="Horário de Saída", help_text='HH:MM', null=True)
   cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
   foto = models.ImageField(upload_to="get_file_path", null=True, blank=True, verbose_name='Foto')


   def __str__(self):
       return self.nome

   class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

class Telefone(models.Model):
    TIPO_CHOICES = (
        ('funcionario', 'Funcionário'),
        ('cliente', 'Cliente'),
    )

    numero = models.CharField(max_length=20, verbose_name="Número de Telefone")
    tipo = models.CharField(max_length=11, choices=TIPO_CHOICES, verbose_name="Tipo", default='cliente')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Telefone: {self.numero}"

    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"

class Endereco(models.Model):
    TIPO_CHOICES = (
        ('funcionario', 'Funcionário'),
        ('cliente', 'Cliente'),
    )

    logradouro = models.CharField(max_length=50, verbose_name="Logradouro")
    numero = models.CharField(max_length=4, verbose_name="Número")
    bairro = models.CharField(max_length=50, verbose_name="Bairro")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    estado = models.CharField(max_length=50, verbose_name="Estado")
    pais = models.CharField(max_length=50, verbose_name="País")
    cep = models.CharField(max_length=8, verbose_name="CEP")
    tipo = models.CharField(max_length=11, choices=TIPO_CHOICES, verbose_name="Tipo", default='Cliente')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Endereço: {self.logradouro}, {self.numero}, {self.cidade}, {self.estado}, {self.pais}"

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

class ContraCheque(models.Model):
    mes_de_referencia = models.IntegerField(verbose_name="Mês de referência")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='contracheques')
    verbas = models.ManyToManyField('Verbas', related_name='contracheques')

    def __str__(self):
        return f"ContraCheque - {self.mes_de_referencia} - {self.funcionario.nome}"

    class Meta:
        verbose_name = "Contra Cheque"
        verbose_name_plural = "Contra Cheques"

class Verbas(models.Model):
    TIPO_CHOICES = (
        ('provento', 'Provento'),
        ('desconto', 'Desconto'),
        ('demonstrativa', 'Demonstrativa'),
    )

    nome = models.CharField(max_length=50, verbose_name="Nome da Verba", default='Verba')
    tipo = models.CharField(max_length=13, choices=TIPO_CHOICES, verbose_name="Tipo", default='provento')
    valor = models.IntegerField(verbose_name="Valor da Verba", default=0)

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()} - Valor: {self.valor}"

    class Meta:
        verbose_name = "Verba"
        verbose_name_plural = "Verbas"
