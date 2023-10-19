# Generated by Django 4.2.6 on 2023-10-19 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0022_alter_cliente_options_alter_contracheque_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='horario_entrada',
            field=models.TimeField(help_text='HH:MM', null=True, verbose_name='Horário de Entrada'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='horario_saida',
            field=models.TimeField(help_text='HH:MM', null=True, verbose_name='Horário de Saída'),
        ),
    ]
