# Generated by Django 3.1.4 on 2021-05-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0004_auto_20210507_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='passport',
            field=models.ImageField(blank=True, upload_to='staff/passports/'),
        ),
    ]