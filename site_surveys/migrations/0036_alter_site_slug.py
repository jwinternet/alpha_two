# Generated by Django 5.0.3 on 2024-03-31 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0035_alter_site_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
