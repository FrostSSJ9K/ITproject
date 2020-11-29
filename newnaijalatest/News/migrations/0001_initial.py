# Generated by Django 2.0.3 on 2018-07-30 11:13

import News.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('body', models.TextField()),
                ('category', models.CharField(choices=[('politics', 'POLITICS'), ('entertainment', 'ENTERTAINMENT'), ('sports', 'SPORT')], default='politics', max_length=15)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('cover_image', models.ImageField(upload_to=News.models.user_directory_path)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('poster', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
