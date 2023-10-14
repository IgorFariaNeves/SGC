# Generated by Django 4.2.5 on 2023-10-13 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0019_pessoajuridica_notafiscal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoajuridica',
            name='notafiscal',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], default='PF', max_length=2, verbose_name='Tipo de Cliente'),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='cliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='aplic.cliente'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='cliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='aplic.cliente'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='aplic.proprietario'),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='Digite o CPF'),
        ),
    ]