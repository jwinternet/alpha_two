# Generated by Django 5.0.3 on 2024-03-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0022_site_back_site_left_site_right'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='title',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]