# Generated by Django 4.2.5 on 2023-10-12 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0006_alter_endereco_funcionario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.cliente'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.cliente'),
        ),
    ]
