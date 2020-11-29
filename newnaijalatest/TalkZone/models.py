from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from  ckeditor.fields import RichTextField, CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class TalkZone(models.Model):
    title = RichTextField(max_length=1000, config_name='special')
    slug = models.SlugField(max_length=1000, unique=True)
    description = RichTextField(max_length=2000, config_name='special')
    body = RichTextUploadingField(config_name='default',
                                  external_plugin_resources=[('Youtube',
                                                              '/NaijaLatest/static/ckeditor/ckeditor/plugins/youtube/',
                                                              'plugin.js', )],
                                  )
    cover_image = models.ImageField(upload_to=user_directory_path, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    poster = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='talkzone', on_delete=models.DO_NOTHING)
    publish = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TalkZone, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comments(models.Model):
    talk_zone = models.ForeignKey(TalkZone, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name