# Generated by Django 2.0.3 on 2018-07-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0005_auto_20180730_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsposts',
            name='poster',
        ),
        migrations.AddField(
            model_name='newsposts',
            name='speaker',
            field=models.CharField(default='private', max_length=100),
        ),
    ]
