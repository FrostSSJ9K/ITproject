# Generated by Django 2.0.3 on 2018-11-16 15:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0033_auto_20181116_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mixtape',
            name='tracks',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='add youtube link here', max_length=5000),
        ),
    ]
