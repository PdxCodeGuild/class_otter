# Generated by Django 4.0.3 on 2022-03-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GLapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desccription', models.TextField(max_length=500, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('completion', models.BooleanField()),
            ],
        ),
    ]
