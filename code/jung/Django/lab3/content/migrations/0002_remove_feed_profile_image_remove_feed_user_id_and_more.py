# Generated by Django 4.0.2 on 2022-03-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='user_id',
        ),
        migrations.AddField(
            model_name='feed',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
