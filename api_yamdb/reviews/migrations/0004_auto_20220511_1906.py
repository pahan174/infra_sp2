# Generated by Django 2.2.16 on 2022-05-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220511_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
