# Generated by Django 4.1 on 2022-08-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_pics/'),
        ),
    ]
