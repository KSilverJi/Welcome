# Generated by Django 3.0.8 on 2020-09-09 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0003_profilephoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilephoto',
            name='topic',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
