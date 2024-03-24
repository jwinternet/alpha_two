# Generated by Django 5.0.3 on 2024-03-24 20:16

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_surveys', '0004_remove_site_today_date_alter_site_date_added_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
