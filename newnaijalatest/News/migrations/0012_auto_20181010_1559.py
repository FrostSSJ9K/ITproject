# Generated by Django 2.0.3 on 2018-10-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0011_newsposts_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsposts',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
