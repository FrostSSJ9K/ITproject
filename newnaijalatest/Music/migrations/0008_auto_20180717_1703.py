# Generated by Django 2.0.3 on 2018-07-17 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0007_auto_20180717_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='released_date',
            new_name='released_Year',
        ),
    ]
