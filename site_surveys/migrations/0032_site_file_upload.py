# Generated by Django 5.0.3 on 2024-03-31 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0031_alter_site_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='site_surveys/media/%Y/%m/%d/'),
        ),
    ]
