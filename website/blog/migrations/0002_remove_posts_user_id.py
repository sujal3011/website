# Generated by Django 4.1.4 on 2022-12-30 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='user_id',
        ),
    ]
