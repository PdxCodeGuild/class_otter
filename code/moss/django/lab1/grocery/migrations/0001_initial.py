# Generated by Django 3.2 on 2022-02-25 07:44

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
                ('description', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField()),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('completed', models.BooleanField()),
            ],
        ),
    ]
