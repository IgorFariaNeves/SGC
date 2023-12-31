# Generated by Django 4.2.6 on 2023-11-14 22:45

import aplic.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0029_alter_funcionario_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto'),
        ),
    ]
