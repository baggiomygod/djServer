# Generated by Django 3.2.13 on 2022-05-20 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video2gif', '0003_auto_20220520_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gif',
            old_name='video',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='user',
        ),
    ]
