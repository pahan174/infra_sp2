# Generated by Django 2.2.16 on 2022-05-14 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0018_auto_20220514_1045'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='unique_author_review',
        ),
    ]
