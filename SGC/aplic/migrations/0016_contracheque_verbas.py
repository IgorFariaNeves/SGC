# Generated by Django 4.2.5 on 2023-10-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0015_notafiscal_pessoafisica_pessoajuridica_proprietario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contracheque',
            name='verbas',
            field=models.ManyToManyField(related_name='Verbas', to='aplic.verbas'),
        ),
    ]
