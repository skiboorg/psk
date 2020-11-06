# Generated by Django 3.1.2 on 2020-10-20 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20201020_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, null=True, verbose_name='Номер шага')),
                ('text', models.TextField(null=True, verbose_name='Текст')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Шаг для услуги',
                'verbose_name_plural': 'Шаги для услуг',
            },
        ),
        migrations.CreateModel(
            name='ServiceFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='service_img/', verbose_name='Иконка')),
                ('text', models.TextField(null=True, verbose_name='Текст')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Приемущество для услуги',
                'verbose_name_plural': 'Приемущества для услуг',
            },
        ),
    ]
