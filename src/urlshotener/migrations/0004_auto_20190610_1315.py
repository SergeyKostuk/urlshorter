# Generated by Django 2.2.2 on 2019-06-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshotener', '0003_url_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=300),
        ),
    ]
