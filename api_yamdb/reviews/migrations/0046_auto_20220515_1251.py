# Generated by Django 2.2.16 on 2022-05-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0045_auto_20220515_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
