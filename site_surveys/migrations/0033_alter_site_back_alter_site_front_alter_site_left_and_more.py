# Generated by Django 5.0.3 on 2024-03-31 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0032_site_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='back',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=4),
        ),
        migrations.AlterField(
            model_name='site',
            name='front',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=4),
        ),
        migrations.AlterField(
            model_name='site',
            name='left',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=4),
        ),
        migrations.AlterField(
            model_name='site',
            name='right',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=4),
        ),
    ]