# Generated by Django 2.0.3 on 2018-10-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mysteries', '0005_quote_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]