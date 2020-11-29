from django.db import models
from django.contrib.auth.models import Permission, User
# Create your models here.
POSITION_CHOICES = (
    ('top', 'TOP'),
    ('body', 'BODY'),
    ('side', 'SIDE'),
    ('footer', 'FOOTER'),
)

class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=2000)
    message = models.TextField()


class Ad_Provider(models.Model):
    company_name = models.CharField(max_length=1000)
    company_site = models.URLField(max_length=1000)

    def __str__(self):
        return self.company_name


class Ad_image(models.Model):
    image_name = models.CharField(max_length=200)
    ad_image = models.FileField(upload_to='images/',)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, default='body')

    def __str__(self):
        return self.image_name


class Ads(models.Model):
    title = models.CharField(max_length=100)
    advertise_url = models.URLField(max_length=2000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.CharField(max_length=35)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_provider = models.ForeignKey(Ad_Provider, on_delete=models.CASCADE)
    ad_images = models.ManyToManyField(Ad_image)

    def __str__(self):
        return self.title
