# Generated by Django 5.0.3 on 2024-03-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0020_remove_site_age_remove_site_file_upload_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='front',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=4),
            preserve_default=False,
        ),
    ]
