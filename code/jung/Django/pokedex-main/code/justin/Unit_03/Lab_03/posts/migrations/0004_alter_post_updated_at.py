# Generated by Django 4.0.2 on 2022-03-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_user_id_discussion_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
