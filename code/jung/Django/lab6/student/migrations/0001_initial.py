# Generated by Django 4.0.3 on 2022-03-23 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('cohort', models.CharField(max_length=50)),
                ('favorite_topic', models.CharField(max_length=200)),
                ('favorite_teacher', models.CharField(max_length=100)),
                ('capstone', models.URLField()),
            ],
            options={
                'ordering': ['-favorite_topic'],
            },
        ),
    ]
