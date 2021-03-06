# Generated by Django 2.0.3 on 2018-07-31 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gist', '0004_auto_20180731_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gistpost',
            name='category',
            field=models.CharField(choices=[('comedy', 'COMEDY'), ('relationship', 'RELATIONSHIP'), ('gossip', 'GOSSIP'), ('wedding', 'WEDDING')], default='comedy', max_length=250),
        ),
        migrations.AlterField(
            model_name='gistpost',
            name='seo_title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
