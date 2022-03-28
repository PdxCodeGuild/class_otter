# Generated by Django 3.2 on 2022-02-25 13:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0003_shortcode_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortcode',
            name='url_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shortcode',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 13, 10, 3, 678388, tzinfo=utc)),
        ),
    ]
