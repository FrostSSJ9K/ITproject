# Generated by Django 2.0.3 on 2018-10-01 07:51

import Music.models
import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Music', '0016_auto_20181001_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mixtape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tape_name', ckeditor.fields.RichTextField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('tape', models.FileField(upload_to=Music.models.user_directory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('tracks', models.CharField(max_length=500)),
                ('dj_description', models.CharField(max_length=500)),
                ('tape_image', ckeditor_uploader.fields.RichTextUploadingField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mixtape', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='mixtapes',
            name='user',
        ),
        migrations.DeleteModel(
            name='Mixtapes',
        ),
    ]