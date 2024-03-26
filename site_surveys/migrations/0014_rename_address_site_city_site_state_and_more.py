# Generated by Django 5.0.3 on 2024-03-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0013_site_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='address',
            new_name='city',
        ),
        migrations.AddField(
            model_name='site',
            name='state',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='street_address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='zip_code',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]