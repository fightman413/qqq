# Generated by Django 3.0.3 on 2020-03-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cateString', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='articleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleTitle', models.CharField(max_length=100)),
                ('articleAuthor', models.CharField(max_length=100)),
                ('articleAbstract', models.CharField(blank=True, max_length=200)),
                ('articleCreateTime', models.DateTimeField()),
                ('articleUpdateTime', models.DateTimeField()),
                ('articleTags', models.ManyToManyField(blank=True, to='articleDetail.Tag')),
            ],
        ),
    ]
