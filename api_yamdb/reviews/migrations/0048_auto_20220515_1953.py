# Generated by Django 2.2.16 on 2022-05-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0047_auto_20220515_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
