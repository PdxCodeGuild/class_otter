# Generated by Django 3.2 on 2022-02-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0003_auto_20220222_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='to_be_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='groceryitem',
            name='to_be_uncompleted',
            field=models.BooleanField(default=False),
        ),
    ]