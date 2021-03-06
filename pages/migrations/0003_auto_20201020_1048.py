# Generated by Django 3.1.2 on 2020-10-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20201020_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callback',
            name='file',
        ),
        migrations.RemoveField(
            model_name='callback',
            name='service',
        ),
        migrations.AlterField(
            model_name='review',
            name='service',
            field=models.ManyToManyField(blank=True, null=True, related_name='review_img', to='pages.Service', verbose_name='Отзыв для услуг'),
        ),
    ]
