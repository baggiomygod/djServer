# Generated by Django 3.2.13 on 2022-08-02 10:03

from django.db import migrations, models
import utils.FileFieldValidators


class Migration(migrations.Migration):

    dependencies = [
        ('video2gif', '0004_auto_20220520_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gif',
            name='url',
            field=models.ImageField(upload_to='D:\\work\\jyjs-projects\\examples\\python\\djserver\\files\\images'),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(upload_to='D:\\work\\jyjs-projects\\examples\\python\\djserver\\files\\video', validators=[utils.FileFieldValidators.validate_file_extension, utils.FileFieldValidators.file_size]),
        ),
    ]
