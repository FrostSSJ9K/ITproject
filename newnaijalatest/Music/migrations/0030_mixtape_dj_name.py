# Generated by Django 2.0.3 on 2018-10-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0029_auto_20181012_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='mixtape',
            name='dj_name',
            field=models.CharField(default='Dj Appostle', max_length=20),
        ),
    ]
