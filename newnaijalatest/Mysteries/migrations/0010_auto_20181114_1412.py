# Generated by Django 2.0.3 on 2018-11-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mysteries', '0009_auto_20181111_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='category',
            field=models.CharField(choices=[('quote', 'QUOTE'), ('poem', 'POEM'), ('letters', 'LETTERS'), ('soulawakening', 'SOULAWAKENING')], default='love', max_length=20),
        ),
    ]