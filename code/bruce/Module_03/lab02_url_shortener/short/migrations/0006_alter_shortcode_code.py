# Generated by Django 3.2 on 2022-02-25 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0005_auto_20220225_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortcode',
            name='code',
            field=models.CharField(blank=True, max_length=200, unique=True, verbose_name='short code'),
        ),
    ]
