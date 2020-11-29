# Generated by Django 2.0.3 on 2018-11-11 13:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gist', '0010_auto_20181012_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gistpost',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='gistpost',
            name='poster',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gistpost',
            name='seo_title',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='gistpost',
            name='slug',
            field=models.SlugField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='gistpost',
            name='title',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
    ]