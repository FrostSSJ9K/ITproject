# Generated by Django 2.0.3 on 2018-09-28 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0013_auto_20180927_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='about_song',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]