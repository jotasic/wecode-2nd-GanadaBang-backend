# Generated by Django 3.2.4 on 2021-06-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_location_dong_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.RemoveField(
            model_name='location',
            name='dong',
        ),
        migrations.RemoveField(
            model_name='location',
            name='state',
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
