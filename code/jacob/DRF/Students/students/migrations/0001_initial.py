# Generated by Django 3.2 on 2022-03-23 22:47

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
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Cohort', models.CharField(max_length=100)),
                ('FavoriteTopic', models.CharField(max_length=200)),
                ('FavoriteTeacher', models.CharField(max_length=200)),
                ('Capstone', models.URLField()),
            ],
        ),
    ]
