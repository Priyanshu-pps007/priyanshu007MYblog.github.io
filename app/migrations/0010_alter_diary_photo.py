# Generated by Django 4.0.3 on 2022-05-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_diary_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='photo',
            field=models.ImageField(default='', null=True, upload_to='media/images/'),
        ),
    ]
