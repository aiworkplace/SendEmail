# Generated by Django 2.2 on 2020-01-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0011_auto_20200104_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
