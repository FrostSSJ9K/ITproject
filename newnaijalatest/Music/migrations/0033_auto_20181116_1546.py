# Generated by Django 2.0.3 on 2018-11-16 14:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0032_auto_20181111_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mixtape',
            name='tracks',
            field=ckeditor.fields.RichTextField(default='add youtube link here', max_length=5000),
        ),
    ]