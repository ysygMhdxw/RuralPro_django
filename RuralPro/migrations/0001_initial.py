# Generated by Django 4.0.3 on 2022-04-04 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testNews',
            fields=[
                ('Title', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='title')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('createTime', models.CharField(max_length=255, verbose_name='createTime')),
                ('editor', models.CharField(max_length=500, verbose_name='editor')),
                ('digest', models.CharField(max_length=1000, verbose_name='digest')),
            ],
        ),
    ]
