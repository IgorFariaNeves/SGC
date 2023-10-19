from django.contrib import admin
from .models import *

class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1

class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline, EnderecoInline]

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline, EnderecoInline]

# Agora você pode continuar com os seus registros existentes:
admin.site.register(ContraCheque)
admin.site.register(Verbas)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(NotaFiscal)
admin.site.register(Proprietario)
