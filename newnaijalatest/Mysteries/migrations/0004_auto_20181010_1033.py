# Generated by Django 2.0.3 on 2018-10-10 09:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mysteries', '0003_auto_20180902_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='message',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]