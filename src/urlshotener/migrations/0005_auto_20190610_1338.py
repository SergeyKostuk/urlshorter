# Generated by Django 2.2.2 on 2019-06-10 13:38

from django.db import migrations, models
import urlshotener.models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshotener', '0004_auto_20190610_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(default=urlshotener.models.generate_url, max_length=300),
        ),
    ]
