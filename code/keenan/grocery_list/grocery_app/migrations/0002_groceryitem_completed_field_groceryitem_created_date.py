# Generated by Django 4.0.2 on 2022-02-24 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='completed_field',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
