# Generated by Django 4.2.6 on 2023-10-19 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0026_notafiscal_pessoajuridica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='contato',
        ),
    ]