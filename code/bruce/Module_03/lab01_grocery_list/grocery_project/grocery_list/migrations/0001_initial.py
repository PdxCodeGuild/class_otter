# Generated by Django 3.2 on 2022-02-18 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('completed_date', models.DateTimeField(verbose_name='date completed')),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
