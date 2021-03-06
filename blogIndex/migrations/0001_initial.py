# Generated by Django 3.0.3 on 2020-03-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleTitle', models.CharField(max_length=100)),
                ('articleAuthor', models.CharField(max_length=50)),
                ('articleAbstract', models.CharField(blank=True, max_length=200)),
                ('articleTags', models.CharField(blank=True, max_length=200)),
                ('articleContent', models.TextField()),
                ('articleCagetoryID', models.CharField(max_length=50)),
                ('articleCagetoryName', models.CharField(max_length=50)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageCarouselImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
