# Generated by Django 2.2.16 on 2022-05-14 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0039_auto_20220514_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('slug',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('slug',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='titles',
            options={'ordering': ('name',)},
        ),
    ]
