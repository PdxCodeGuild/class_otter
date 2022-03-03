# Generated by Django 3.2 on 2022-02-26 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0003_auto_20220225_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshort',
            name='times_followed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='urlshort',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
