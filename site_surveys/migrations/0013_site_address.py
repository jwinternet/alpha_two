# Generated by Django 5.0.3 on 2024-03-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0012_alter_site_site_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
