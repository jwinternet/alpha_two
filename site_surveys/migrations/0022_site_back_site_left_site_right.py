# Generated by Django 5.0.3 on 2024-03-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0021_site_front'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='back',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='left',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='right',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=4),
            preserve_default=False,
        ),
    ]