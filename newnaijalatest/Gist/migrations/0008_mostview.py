# Generated by Django 2.0.3 on 2018-08-23 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gist', '0007_auto_20180813_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_viewd', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Gist.GistPost')),
            ],
        ),
    ]