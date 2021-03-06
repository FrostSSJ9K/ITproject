# Generated by Django 2.0.3 on 2018-07-17 10:47

import Music.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to=Music.models.user_directory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('cover_image', models.ImageField(upload_to=Music.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=Music.models.user_directory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('cover_image', models.ImageField(upload_to=Music.models.user_directory_path)),
            ],
        ),
        migrations.AlterField(
            model_name='music',
            name='cover_image',
            field=models.ImageField(upload_to='cover_image/'),
        ),
        migrations.AlterField(
            model_name='music',
            name='song_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='video',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.Music'),
        ),
        migrations.AddField(
            model_name='video',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='videos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='audio',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.Music'),
        ),
        migrations.AddField(
            model_name='audio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='audios', to=settings.AUTH_USER_MODEL),
        ),
    ]
