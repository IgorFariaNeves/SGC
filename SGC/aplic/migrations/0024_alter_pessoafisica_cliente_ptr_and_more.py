# Generated by Django 4.2.6 on 2023-10-19 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0023_alter_funcionario_horario_entrada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoafisica',
            name='cliente_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.cliente'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='cliente_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.cliente'),
        ),
    ]
