# Generated by Django 3.1.2 on 2020-11-22 13:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20201122_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='seotag',
            name='aboutText',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст на страницу о нас'),
        ),
    ]
