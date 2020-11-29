# Generated by Django 2.0.3 on 2018-10-06 21:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TalkZone', '0010_auto_20181006_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='slug',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='talkzone',
            name='subbody',
            field=ckeditor.fields.RichTextField(max_length=250),
        ),
    ]