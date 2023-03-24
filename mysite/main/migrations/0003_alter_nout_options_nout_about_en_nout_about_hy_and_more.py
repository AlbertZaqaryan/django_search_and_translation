# Generated by Django 4.1.7 on 2023-03-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_nout_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nout',
            options={'ordering': ['price'], 'verbose_name': 'Nout', 'verbose_name_plural': 'Nouts'},
        ),
        migrations.AddField(
            model_name='nout',
            name='about_en',
            field=models.TextField(null=True, verbose_name='Nout about'),
        ),
        migrations.AddField(
            model_name='nout',
            name='about_hy',
            field=models.TextField(null=True, verbose_name='Nout about'),
        ),
        migrations.AddField(
            model_name='nout',
            name='about_ru',
            field=models.TextField(null=True, verbose_name='Nout about'),
        ),
        migrations.AddField(
            model_name='nout',
            name='name_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Nout name'),
        ),
        migrations.AddField(
            model_name='nout',
            name='name_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Nout name'),
        ),
        migrations.AddField(
            model_name='nout',
            name='name_ru',
            field=models.CharField(max_length=60, null=True, verbose_name='Nout name'),
        ),
    ]