# Generated by Django 4.0.2 on 2022-03-03 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_bookmark_like_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='like_count',
        ),
    ]
