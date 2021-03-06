# Generated by Django 3.0.4 on 2020-07-06 12:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200417_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('uid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('focus_time', models.CharField(max_length=20)),
                ('interrupt_time', models.CharField(max_length=20)),
                ('singer', models.CharField(max_length=20)),
                ('songs_name', models.CharField(max_length=20)),
                ('interrupt', models.CharField(max_length=20)),
                ('openid', models.CharField(max_length=120)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeedRecorded',
            fields=[
                ('uid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('openid', models.CharField(max_length=120)),
                ('singer', models.CharField(max_length=20)),
                ('songs_name', models.CharField(max_length=20)),
                ('focusTime', models.CharField(max_length=20)),
                ('interruptTime', models.CharField(max_length=20)),
                ('interrupt', models.CharField(max_length=20)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planType', models.BooleanField(default=False)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='MusicCode',
            field=models.CharField(default='', max_length=20),
        ),
    ]
