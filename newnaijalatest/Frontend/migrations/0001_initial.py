# Generated by Django 2.0.3 on 2019-04-12 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('ad_image', models.FileField(upload_to='images/')),
                ('position', models.CharField(choices=[('top', 'TOP'), ('body', 'BODY'), ('side', 'SIDE'), ('footer', 'FOOTER')], default='body', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ad_Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1000)),
                ('company_site', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('advertise_url', models.URLField(max_length=2000)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('category', models.CharField(max_length=35)),
                ('ad_images', models.ManyToManyField(to='Frontend.Ad_image')),
                ('ad_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Frontend.Ad_Provider')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=2000)),
                ('message', models.TextField()),
            ],
        ),
    ]
