# Generated by Django 4.2.6 on 2023-11-14 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0028_funcionario_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='get_file_path', verbose_name='Foto'),
        ),
    ]
