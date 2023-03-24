# Generated by Django 4.1.7 on 2023-03-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nout name')),
                ('price', models.PositiveBigIntegerField(verbose_name='Nout price')),
                ('img', models.ImageField(upload_to='images', verbose_name='Nout image')),
                ('about', models.TextField(verbose_name='Nout about')),
                ('check_nout', models.BooleanField(verbose_name='Nout check Yes/No')),
            ],
            options={
                'verbose_name': 'Nout',
                'verbose_name_plural': 'Nouts',
            },
        ),
    ]
