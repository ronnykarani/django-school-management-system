# Generated by Django 3.1.4 on 2021-05-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to='passports/'),
        ),
    ]
