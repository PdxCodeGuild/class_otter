# Generated by Django 3.2 on 2022-02-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortcode',
            name='code',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shortcode',
            name='url',
            field=models.URLField(),
        ),
    ]
