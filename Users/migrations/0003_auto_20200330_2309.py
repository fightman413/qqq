# Generated by Django 3.0.4 on 2020-03-30 15:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_users_jurisdiction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AddField(
            model_name='users',
            name='user_id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
