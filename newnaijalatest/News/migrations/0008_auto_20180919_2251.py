# Generated by Django 2.0.3 on 2018-09-19 21:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_auto_20180730_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsposts',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
