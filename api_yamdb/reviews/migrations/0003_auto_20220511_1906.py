# Generated by Django 2.2.16 on 2022-05-11 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220511_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='titles',
            name='description',
            field=models.TextField(default='Default_description'),
        ),
        migrations.AddField(
            model_name='titles',
            name='name',
            field=models.TextField(default='Default_name'),
        ),
        migrations.AddField(
            model_name='titles',
            name='year',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='titles',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category'),
        ),
        migrations.AddField(
            model_name='titles',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Genre'),
        ),
    ]
