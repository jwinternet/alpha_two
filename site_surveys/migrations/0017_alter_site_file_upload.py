# Generated by Django 5.0.3 on 2024-03-26 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0016_alter_site_age_alter_site_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='site_surveys/media/%Y/%m/%d/'),
        ),
    ]
