# Generated by Django 4.1.2 on 2022-10-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20211129_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='default/avatat.png', null=True, upload_to='profile_images'),
        ),
    ]
