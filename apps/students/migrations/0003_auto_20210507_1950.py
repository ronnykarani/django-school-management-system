# Generated by Django 3.1.4 on 2021-05-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20201124_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='passport',
            field=models.ImageField(blank=True, upload_to='passports/'),
        ),
        migrations.AlterField(
            model_name='studentbulkupload',
            name='csv_file',
            field=models.FileField(upload_to='bulkupload/students/'),
        ),
    ]