# Generated by Django 2.0.3 on 2018-09-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mysteries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lovequote',
            name='category',
            field=models.CharField(choices=[('love', 'LOVE'), ('inspirational', 'INSPIRATIONAL'), ('motivational', 'MOTIVATIONAL'), ('insight', 'INSIGHT')], default='love', max_length=15),
        ),
    ]
