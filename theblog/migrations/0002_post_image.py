# Generated by Django 2.2 on 2019-06-22 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='1.png', upload_to='images/%Y/%m/%d'),
        ),
    ]
