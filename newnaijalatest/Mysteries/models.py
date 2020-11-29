from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from  ckeditor.fields import RichTextField, CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)
# Create your models here.


CATEGORY_CHOICES = (
    ('quote', 'QUOTE'),
    ('poem', 'POEM'),
    ('letters', 'LETTERS'),
    ('soul awakening', 'SOUL AWAKENING')
)


class Quote(models.Model):
    message = RichTextUploadingField(config_name='default',
                                     external_plugin_resources=[('Youtube',
                                                                '/NaijaLatest/static/ckeditor/ckeditor/plugins/youtube/',
                                                                 'plugin.js',)],


                                     )
    quote_picture = models.ImageField(upload_to=user_directory_path, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='love')
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mysteries', on_delete=models.DO_NOTHING)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.category
