# Generated by Django 2.0.3 on 2018-08-13 01:45

import Gist.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gist', '0005_auto_20180731_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comedy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comedy', models.FileField(upload_to=Gist.models.user_directory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gistpost',
            name='category',
            field=models.CharField(choices=[('gossip', 'GOSSIP'), ('relationship', 'RELATIONSHIP'), ('wedding', 'WEDDING'), ('celeb', 'CELEB')], default='comedy', max_length=250),
        ),
        migrations.AddField(
            model_name='comedy',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gist.GistPost'),
        ),
        migrations.AddField(
            model_name='comedy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comedy', to=settings.AUTH_USER_MODEL),
        ),
    ]
