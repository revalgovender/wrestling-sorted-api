# Generated by Django 5.0 on 2023-12-30 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('episode_date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TvShow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('playlist_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(unique=True)),
                ('thumbnail_default', models.URLField(default=None, null=True)),
                ('thumbnail_medium', models.URLField(default=None, null=True)),
                ('thumbnail_high', models.URLField(default=None, null=True)),
                ('thumbnail_maxres', models.URLField(default=None, null=True)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wrestling_sorted.episode')),
                ('tv_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wrestling_sorted.tvshow')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='tv_show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wrestling_sorted.tvshow'),
        ),
    ]
